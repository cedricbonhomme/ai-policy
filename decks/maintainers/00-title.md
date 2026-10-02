# `ai-policy.yml`

## Machine-readable rules of engagement for AI contributions

Lukas Kahwe Smith - [lukas.smith@bfh.ch](mailto:lukas.smith@bfh.ch)

[Bern University of Applied Sciences<br />
Institute for Public Sector Transformation](https://www.bfh.ch/de/forschung/forschungsbereiche/public-sector-transformation/)

For open source maintainers

<!-- .slide: class="title-slide" data-timing="30" -->

Note:

- Maintained deck: no venue line, because it outlives any one talk. Add a venue variant of this title alongside it and swap it in `deck.json` before presenting
- The claim in one line: **one small file in your repository tells agents, CI checks and people what your project permits for AI contributions, before anyone opens a pull request**
- Say early that this is an early proposal with the design not settled: a convention to prove out through adoption, not a standard to ratify
- The arc: what the file is and where it lives, its main fields, starting from a preset or working a policy out, how a consumer resolves it, validating it, and what tools can do with it
- The why and the design principles are the subject of the sibling ecosystem deck; this one is hands-on
