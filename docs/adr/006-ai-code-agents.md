# ADR-006: AI Code Agents

| Creation Date | Status   | Author                                 |
| :-----------: | :------: | :------------------------------------: |
| 18/06/2026    | Accepted | [@mclargo](https://github.com/McLargo) |

## Context and Problem Statement

Right now, IA code agents is a must have on your project. Some way or another,
they help with code generation, documentation and testing. Plus, they can help
with code review and quality assurance, seeing some issues that humans may not
see.

This project is the perfect candidate to use an AI code agent, as it has a lot
of code and documentation to review. The goal is to configure the basics context
for an AI code agent, so it can understand the project and help with common
tasks and review current lessons.

## Solutions

As I am using github-copilot integrated in my IDE (VSCode), I will ask copilot
to understand the project and generate a context file
`AGENTS.md`, so it can be used in future prompts.

`AGENTS.md` file needs to be reviewed and approved by a human,
to confirm the context is correct and complete. After that, I've also asked
copilot to review all the lessons, generate a report of the quality of the
lessons and suggest improvements. Plan to tackle improvements is defined in
`docs/plans/IMPROVEMENT_PLAN.md`.

## Other Solutions Considered

Claude is the other AI code agent I have used, and it is very good. But the
license is not free, and I think github copilot is enough for this project.
