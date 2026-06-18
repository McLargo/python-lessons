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

## Lessons Quality

A comprehensive quality review was conducted on all Python lessons using the
criteria defined in AGENTS.md. Each lesson was evaluated across four weighted
categories: Technical Accuracy (35%), Code Quality (25%), Educational Value
(25%), and Documentation (15%).

### Overall Summary Table

| Level | Lesson | Tech Accuracy (35%) | Code Quality (25%) | Educational (25%) | Docs (15%) | **Score (10)** | Status |
| ------- | -------- | --------------------- | ------------------- | ------------------ | ------------ | ---------------- | -------- |
| **Beginner** | Classes & Objects | 32 | 22 | 21 | 13 | **8.8** | ✅ Excellent |
| | Dataclasses | 28 | 23 | 22 | 14 | **8.7** | ✅ Excellent |
| | Dict vs DefaultDict | 28 | 20 | 20 | 13 | **8.1** | ✅ Good |
| | Check isinstance | 25 | 18 | 10 | 5 | **5.8** | ⚠️ Needs Work |
| **Intermediate** | Logging | 30 | 22 | 24 | 14 | **9.0** | ⭐ Outstanding |
| | Yield vs Return | 32 | 22 | 19 | 12 | **8.5** | ✅ Excellent |
| | Exceptions | 20 | 18 | 22 | 11 | **7.1** | ⚠️ Good/Needs Work |
| **Advanced** | Behavioral Patterns | 32 | 20 | 22 | 13 | **8.7** | ✅ Excellent |
| | Concurrency/Parallelism | 33 | 18 | 21 | 13 | **8.5** | ✅ Excellent |
| | Lambda Functions | 28 | 19 | 16 | 10 | **7.3** | ⚠️ Good/Needs Work |
| | Decorators | 24 | 18 | 17 | 10 | **6.9** | ⚠️ Acceptable |

### Statistics by Level

| Level | Avg Score | Range | Best Lesson | Needs Most Work |
| ------- | ----------- | ------- | ------------- | ----------------- |
| **Beginner** | **7.9/10** | 5.8 - 8.8 | Classes & Objects (8.8) | Check isinstance (5.8) |
| **Intermediate** | **8.0/10** | 7.1 - 9.0 | Logging (9.0) ⭐ | Exceptions (7.1) |
| **Advanced** | **7.9/10** | 6.9 - 8.5 | Concurrency/Parallelism | Decorators (6.9) |
| **Overall** | **7.9/10** | 6.9 - 9.0 | - | - |

## ADR

Architecture Decision Records (ADR) are used to document the architectural
decisions taken on the project. They are located in the `docs/adr` folder.

- ADR-001: [poetry](docs/adr/001-poetry.md)
- ADR-002: [mkdocs](docs/adr/002-mkdocs.md)
- ADR-003: [cSpell](docs/adr/003-spelling.md)
- ADR-004: [Deployment](docs/adr/004-deployment.md)
- ADR-005: [Dependency Maintenance](docs/adr/005-maintenance.md)
- ADR-006: [AI Code Agents](docs/adr/006-ai-code-agents.md)

## Structure

The code is written in Python, and the documentation is written in Markdown. The
structure of the code is simple:

- All the markdown files are located in the `docs` folder.
- The code is located in the `src` folder.
- Test are located in the `tests` folder.

Other folders and files are used to configure the project or help to maintain
and develop it.

## Testing

Test are mandatory for all code, and they are required to have 100% of coverage.
All tests are located in the `tests` folder, and they mirror the structure of
the `src` folder. Tests are written using [pytest](https://docs.pytest.org/). To
run the tests, use `make test`.

Coverage report is generated using
[coverage.py](https://coverage.readthedocs.io/). To generate the coverage
report, use `make coverage`.

Mutation tests are generated using [mutmut](https://mutmut.readthedocs.io/). To
run mutation tests use `make mutations`. I don't expect to have 100% of mutation
coverage as it is a example repository, but it is a good practice to have it as
high as possible.

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

## Renovate

Renovate bot is used to keep dependencies up to date. It is configured to check
for updates once a week. Configuration file is located in `renovate.json`.
