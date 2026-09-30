# /// script
# requires-python = ">=3.10"
# dependencies = ["jsonschema", "pyyaml"]
# ///
"""Map the labelled corpus of Hora, Robbes and Zacchiroli (2026) to ai-policy records.

Fetches the CC BY 4.0 dataset from Zenodo, turns each of its 281 labelled
policies into the partial `ai-policy.yml` its labels support, validates every
record against the schema, and reports what mapped and what did not.

    uv run research/hora-2026/map.py [--out DIR]

`--out` also writes one JSON record per policy, for inspection.
"""
import argparse
import csv
import io
import json
import pathlib
import urllib.request
from collections import Counter

import jsonschema
import yaml

RECORD = "22212208"  # https://doi.org/10.5281/zenodo.22212208
FILE = "dataset1-multiple-ai-policies.csv"
URL = f"https://zenodo.org/records/{RECORD}/files/{FILE}?download=1"
SCHEMA = pathlib.Path(__file__).resolve().parents[2] / "ai-policy.schema.yaml"

# The paper's countermeasure labels this format carries, and where.
ENFORCEMENT = {"close": "maintainer-review", "ban": "denylist", "block": "denylist", "report": "denylist"}
CONTENT = {"tool", "model", "extent", "usage"}


def column(rows, prefix):
    return next(c for c in rows[0] if c.startswith(prefix))


def label(row, col):
    return (row[col] or "").strip().lower()


def items(row, col):
    return [t.strip() for t in (row[col] or "").split(",") if t.strip()]


def stance(value):
    return {"forbidden": "disallowed", "permitted": "generated", "encouraged": "generated"}.get(value)


def map_row(row, cols, gaps, mapped):
    doc, defaults, scopes, notes = {"version": 1}, {}, {}, []
    exceptions = False

    s = stance(label(row, cols["code"]))
    if s:
        defaults["stance"] = s  # `encouraged` is `generated`: stance is permission, not preference
        mapped["code"] += 1
    for key, scope_names in (("communication", ["comments"]), ("issues", ["issue-descriptions", "security-reports"])):
        value = label(row, cols[key])
        if value == "unclear":
            exceptions = True
            gaps[f"{key}: unclear"] += 1
        elif stance(value):
            mapped[key] += 1
            for name in scope_names:
                scopes[name] = {"scope": name, "stance": stance(value)}

    value = label(row, cols["disclosure"])
    if value in ("yes", "no"):
        defaults["disclosure"] = "required" if value == "yes" else "none"
        mapped["disclosure"] += 1
    elif value == "unclear":
        exceptions = True
        gaps["disclosure: unclear"] += 1
    fmt = {}
    locations = items(row, "Location")
    if locations:
        fmt["method"] = sorted({"commit-trailer" if loc == "commit" else "free-text" for loc in locations})
        mapped["disclosure location"] += 1
    content = items(row, "Content")
    if CONTENT & set(content):
        fmt["content"] = sorted(CONTENT & set(content))
        mapped["disclosure content"] += 1
    for other in set(content) - CONTENT:
        gaps[f"disclosure content: {other}"] += 1
    if fmt:
        doc["disclosureFormat"] = fmt

    if label(row, cols["accountability"]) == "yes":
        defaults["accountability"] = "contributor"
        mapped["accountability"] += 1
    value = label(row, cols["involvement"])
    if value == "high":
        defaults["humanReview"] = "required"
        mapped["human involvement"] += 1
    elif value == "low":
        defaults["humanReview"] = "none"
        doc.setdefault("autonomousAgents", {})["allowed"] = True
        mapped["human involvement"] += 1
    elif value == "medium":
        gaps["human involvement: medium (prompting only)"] += 1
        notes.append("human involvement limited to prompting")

    mechanisms = set()
    for measure in items(row, "Slop Solution"):
        if measure in ENFORCEMENT:
            mechanisms.add(ENFORCEMENT[measure])
        elif measure == "no autonomous agent":
            doc.setdefault("autonomousAgents", {})["allowed"] = False
        elif measure == "approval":
            doc["priorArrangement"] = {"appliesTo": ["ai-generated-prs"], "basis": "reviewer-agreement"}
        elif measure == "contributor":
            # The label covers new and external contributors alike; the stance
            # it implies is in the excerpt, not the label.
            doc["newContributors"] = {"notes": "AI contributions from new or external contributors are restricted"}
            exceptions = True
            gaps["countermeasure: contributor (field exists, stance not in the label)"] += 1
            continue
        else:
            gaps[f"countermeasure: {measure}"] += 1
            notes.append(f"countermeasure: {measure}")
            continue
        mapped[f"countermeasure: {measure}"] += 1
    if mechanisms:
        doc["enforcement"] = {"mechanism": sorted(mechanisms)}

    if notes:
        defaults["notes"] = "; ".join(notes)
        exceptions = True
    if defaults:
        doc["defaults"] = defaults
    if scopes:
        doc["assertions"] = list(scopes.values())
    if exceptions:
        doc["exceptions"] = True
    if "stance" in defaults:
        doc["summary"] = summary(doc)
    return doc


def summary(doc):
    s = doc["defaults"]["stance"]
    if s != "generated":
        return {"disallowed": "disallowed", "assisted": "restrictive"}[s]
    condition = (
        doc["defaults"].get("disclosure") in ("required", "prohibited")
        or doc.get("priorArrangement")
        or any(a["stance"] != "generated" for a in doc.get("assertions", []))
    )
    return "mixed" if condition else "permissive"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=pathlib.Path)
    args = parser.parse_args()

    with urllib.request.urlopen(URL) as response:
        rows = list(csv.DictReader(io.StringIO(response.read().decode("utf-8"))))
    cols = {
        "code": column(rows, "AI policy for code"),
        "communication": column(rows, "AI policy for comunication"),  # spelling as in the dataset
        "issues": column(rows, "AI policy for issues"),
        "disclosure": column(rows, "AI disclosure obligation"),
        "accountability": column(rows, "Accountability"),
        "involvement": column(rows, "Level of human"),
    }
    validator = jsonschema.Draft202012Validator(yaml.safe_load(SCHEMA.read_text()))

    gaps, mapped, invalid, complete, summaries = Counter(), Counter(), [], 0, Counter()
    for row in rows:
        doc = map_row(row, cols, gaps, mapped)
        if list(validator.iter_errors(doc)):
            invalid.append(row["repo"])
        elif not doc.get("exceptions"):
            complete += 1
        summaries[doc.get("summary", "(no default stance)")] += 1
        if args.out:
            args.out.mkdir(parents=True, exist_ok=True)
            (args.out / (row["repo"].replace("/", "__") + ".json")).write_text(json.dumps(doc, indent=1))

    print(f"policies: {len(rows)}")
    print(f"schema-valid records: {len(rows) - len(invalid)}; invalid: {', '.join(invalid) or 'none'}")
    print(f"expressed completely (no exceptions): {complete}")
    print("summaries:", dict(summaries))
    print("mapped labels:")
    for key, n in mapped.most_common():
        print(f"  {key}: {n}")
    print("labels the format does not carry:")
    for key, n in gaps.most_common():
        print(f"  {key}: {n}")


if __name__ == "__main__":
    main()
