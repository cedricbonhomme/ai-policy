"""Check the policy files of this repository.

Each file must validate against ai-policy.schema.yaml, and keep to the plain YAML
the README allows (see "Placement"): no anchors, aliases, tags, merge keys, several
documents in one file, or plain or quoted values spread over several lines; blocks
of text introduced by | or > are allowed.

    python tools/validate.py [FILE ...]

Without FILE, every policy file of the repository is checked. Needs PyYAML and
jsonschema. Exits with 1 when a file fails.
"""

from __future__ import annotations

import sys
from pathlib import Path

import jsonschema
import yaml

ROOT = Path(__file__).resolve().parent.parent
SCHEMA = ROOT / "ai-policy.schema.yaml"
DEFAULT = ["ai-policy.example.yaml", "ai-policy.yaml", "examples/*.yaml"]


def plain_yaml(text: str) -> list[str]:
    """What the file uses beyond the plain YAML a policy file may use."""
    problems = []
    documents = 0
    for event in yaml.parse(text):
        line = event.start_mark.line + 1
        if isinstance(event, yaml.DocumentStartEvent):
            documents += 1
        elif isinstance(event, yaml.AliasEvent):
            problems.append(f"line {line}: an alias")
        elif getattr(event, "anchor", None):
            problems.append(f"line {line}: an anchor")
        if isinstance(event, (yaml.ScalarEvent, yaml.CollectionStartEvent)) and event.tag and not (
            event.implicit if isinstance(event, yaml.CollectionStartEvent) else any(event.implicit)
        ):
            problems.append(f"line {line}: a tag")
        if isinstance(event, yaml.ScalarEvent):
            if event.value == "<<" and event.style is None:
                problems.append(f"line {line}: a merge key")
            if event.style in (None, "'", '"') and event.end_mark.line != event.start_mark.line:
                problems.append(f"line {line}: a value spread over several lines")
    if documents > 1:
        problems.append("several documents")
    return problems


def check(path: Path, validator: jsonschema.Draft202012Validator) -> list[str]:
    text = path.read_text(encoding="utf-8")
    try:
        problems = plain_yaml(text)
    except yaml.YAMLError as error:
        return [f"not YAML: {error}"]
    if problems:
        return problems
    data = yaml.safe_load(text)
    for error in sorted(validator.iter_errors(data), key=lambda error: list(error.path)):
        where = "/".join(str(part) for part in error.path) or "the file"
        problems.append(f"{where}: {error.message}")
    return problems


def main(arguments: list[str]) -> int:
    schema = yaml.safe_load(SCHEMA.read_text(encoding="utf-8"))
    jsonschema.Draft202012Validator.check_schema(schema)
    validator = jsonschema.Draft202012Validator(schema)
    paths = [Path(name) for name in arguments] or sorted(
        path for pattern in DEFAULT for path in ROOT.glob(pattern)
    )
    failed = 0
    for path in paths:
        problems = check(path, validator)
        name = path.relative_to(ROOT) if path.is_relative_to(ROOT) else path
        print(f"{name}: {'ok' if not problems else 'FAILED'}")
        for problem in problems:
            print(f"  {problem}")
        failed += bool(problems)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
