# ADR-003 - Spelling check

| Creation Date | Status   | Author                                 |
| :-----------: | :------: | :------------------------------------: |
| 20/02/2024    | Accepted | [@mclargo](https://github.com/McLargo) |

## Context and Problem Statement

Python lessons is a project that contains python code, but mainly documentation.
Either in the format of docstrings attached to the code, or in markdown files.

Main language for the documentation is English, but it is not the native
language of the authors. It is important to have a tool that checks the spelling
of the documentation, to avoid typos and grammar mistakes.

## Solution

[cSpell](https://cspell.org/) is a good tool to check the spelling of files.
There are some features offered by cSpell out-of-the-box that makes the
difference:

- Supports more than one language. It is possible to check the spelling of
  different languages in the same file.
- Supports different file formats, including markdown and python files.
- Supports
  [pre-commit](https://github.com/streetsidesoftware/cspell-cli#setup-pre-commit-hook),
  which is already working in the project, so it is easy to add new rule.
- It is possible to define your own dictionary, and define custom words.
- Compatible with VSCode, which is the main IDE used by the authors.
- Highly configurable.

## Other Solution Considered

- [yaspeller](https://github.com/hcodes/yaspeller): it is a good tool, but it
  does not support multiple languages in the same file and not compatible with
  VSCode.
- [codespell](https://github.com/codespell-project/codespell): much older than
  cSpell, and not as feature-rich. Documentation hard to follow.
