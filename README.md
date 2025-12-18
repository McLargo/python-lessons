# Python lessons

During my many years working as a developer, my main programming language has been
Python. I've learned many cool features during this time, and a few lessons were
learned. Additionally, I have incorporated good practices into my code.

This repository is created to group some of these lessons into different levels
(beginner, intermediate and advanced). Tests are included, so it is easy to
understand and practice with them.

All lessons is [available online](https://mclargo.github.io/python-lessons/) on
the last version.

## Usage

TL;DR: `make install` to install dependencies, `make server` to start mkdocs
server to access documentation.

Makefile is your friend. All commands are available through it, so it is quite
easy and friendly usage. Run `make` or `make help` to get more information for
the commands to use.

## ADR

Architecture Decision Records (ADR) are used to document the architectural
decisions taken on the project. They are located in the `docs/adr` folder.

- ADR-001: [poetry](docs/adr/001-poetry.md)
- ADR-002: [mkdocs](docs/adr/002-mkdocs.md)
- ADR-003: [cSpell](docs/adr/003-spelling.md)
- ADR-004: [Deployment](docs/adr/004-deployment.md)

## Structure

The code is written in Python, and the documentation is written in Markdown. The
structure of the code is simple:

- All the markdown files are located in the `docs` folder.
- The code is located in the `src` folder.
- Test are located in the `tests` folder.

Other folders and files are used to configure the project or help to maintain
and develop it.

## CI/CD

- The project is configured to use GitHub Actions to automatically deploy the
  documentation to [GitHub Pages](https://mclargo.github.io/python-lessons/)
  once code is merged into `master`. The workflow is defined in
  `.github/workflows/ci-deployment.yml`.

## Pre-commit

The project is configured to use [pre-commit](https://pre-commit.com/) to check
Python and markdown files are following the style guide. pre-commit is
automatically installed when running `make install`.

Rules are defined in `.pre-commit-config.yaml` and include:

- [markdownlint](https://github.com/igorshubovych/markdownlint-cli): markdown
    code linter.
- [ruff](https://github.com/astral-sh/ruff-pre-commit): Python code linter and
    formatter. Properly configured, I replaced both black and bandit.
- [cspell](https://github.com/streetsidesoftware/cspell-cli): Spelling checker.
- mkdocs-build: Local hook to make sure mkdocs build is working properly.

If you want to trigger manually the execution, run `pre-commit run --all-files`
to execute all pre-commits checks for all files in the project, or
`pre-commit run -a <hook_id>` to run a specific hook.

## IDE

The project has been developed using
[Visual Studio Code](https://code.visualstudio.com/).

It is not mandatory to use VSCode, but it is recommended. The project includes a
settings file to help to maintain similar settings used during the development.
