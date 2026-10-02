## An agent-tooling problem

- A [pre-flight check](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/README.md#why-this-is-an-agent-tooling-problem-the-consumer-story) before opening a PR
- Read the way a crawler reads `robots.txt`
- Beside `AGENTS.md`, where agents already look
- An MCP server could serve and check it

**May I contribute generated code here?<br />Must I disclose it? May an agent open this PR?**

[↳ README: why this is an agent-tooling problem](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/README.md#why-this-is-an-agent-tooling-problem-the-consumer-story)

Note:

↓ Sanctioned workflows: the other half

**Acronyms:** PR = pull request; MCP = Model Context Protocol, a common way to plug tools and data into AI agents

- The file only matters if something reads it, and the natural readers are coding agents
- Unlike `robots.txt` it declares stance, disclosure and agent-identity rules, not crawl permissions
- The MCP server is a *could*: a reference consumer that serves a repo's file and validates a proposed change against it, so any MCP-speaking agent gets the policy without bespoke parsing
- No such consumer exists yet; building the smallest one is part of the ask

**Q&A details:**

- `AGENTS.md` and `CLAUDE.md` point to the file; a section of `AGENTS.md` is a plausible alternative home, named in the prior-art section

--

## Sanctioned workflows: the other half

<!-- .slide: data-timing="0" -->

- Fedora's AI/ML SIG publishes a [skills library](https://forge.fedoraproject.org/ai-ml/skills-library)
- Approved agent workflows, in the Agent Skills format
- Answers part of the policy in executable form
- Which field points at it is [open](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/README.md#open-questions-named)

**"These workflows are sanctioned here"<br />is more useful than a restatement of the rules.**

Note:

**Acronyms:** SIG = special interest group

- The punchline paraphrases the README; it is not a quotation from Fedora
- Its current skills automate compose triage, FTBFS bug search, meeting-log summarisation and Packit onboarding
- The open question is "Sanctioned-workflow pointer": `guardrailsRef` points at rules a contributor must observe; a skills library names what the project has already blessed. Folding both into one pointer may be right, but the semantics differ

**Q&A details:**

- FTBFS = fails to build from source
- The library is CC BY-SA 4.0; each skill is a directory with a `SKILL.md` carrying YAML frontmatter and instructions
