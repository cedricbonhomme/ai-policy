# Mapping a labelled corpus to `ai-policy`

[`map.py`](./map.py) takes the labelled corpus behind ["We Permit the Use of AI, but […]"](https://arxiv.org/abs/2609.07542) (Hora, Robbes and Zacchiroli, 2026), 281 AI-contribution policies from popular open source projects, and turns each into the partial `ai-policy.yaml` its labels support. It then validates every record against [`ai-policy.schema.yaml`](../../ai-policy.schema.yaml) and reports which labels the format carries and which it does not.

It is a coverage check at a scale no manual survey reaches, and a first demonstration of the [research aim](../../README.md#aims): once policies are declared in one vocabulary, questions like these become a script. Results and what they mean for the format are in [`coverage.md`](../../coverage.md#a-larger-corpus-popular-projects).

```sh
uv run research/hora-2026/map.py            # summary
uv run research/hora-2026/map.py --out out  # also one JSON record per policy
```

The dataset is fetched from [Zenodo](https://doi.org/10.5281/zenodo.22212208) at run time rather than copied here; it is published under CC BY 4.0 by its authors.

## How labels map

- **Code, communication, issues and security:** `forbidden` becomes `disallowed` and `permitted` or `encouraged` becomes `generated`, since a stance states permission, not preference. Code sets `defaults.stance`; communication sets the `comments` scope; issues and security set `issue-descriptions` and `security-reports`.
- **Disclosure:** an explicit yes or no becomes `required` or `none`; the location becomes `disclosureFormat.method`, with a commit as `commit-trailer` and every other place as `free-text`; the content becomes `disclosureFormat.content`.
- **Accountability** becomes `accountability: contributor`; **high human involvement** becomes `humanReview: required`, and **low**, where full automation is welcome, `humanReview: none` with autonomous agents allowed.
- **Countermeasures:** closing pull requests becomes `maintainer-review` enforcement, bans, blocks and denouncing become `denylist`, forbidding autonomous agents sets `autonomousAgents.allowed: false`, and prior approval becomes a `priorArrangement`. Restricting new or external contributors is recorded under `newContributors` as a note only, because the label does not say which stance applies.
- **Labels coded as unclear, and anything without a field,** set `exceptions: true` and go into `notes`.
