# Python lessons

During my many years working as a developer, my main programming language has been
Python. I've learned many cool features during this time, and a few lessons were
learned. Additionally, I have incorporated good practices into my code.

This repository is created to group some of these lessons into different levels
(beginner, intermediate and advanced). Tests are included, so it is easy to
understand and practice with them.

## Usage

TL;DR: `make install` to install dependencies, `make server` to start mkdocs
server to access documentation.

Makefile is your friend. All commands are available through it, so it is quite
easy and friendly usage. Run `make` or `make help` to get more information for
the commands to use.

## ADR

- ADR-001: [poetry](docs/adr/001-poetry.md)
- ADR-002: [mkdocs](docs/adr/002-mkdocs.md)
- ADR-003: [cSpell](docs/adr/003-spelling.md)

## Contributing

- Use [conventional commit](https://www.conventionalcommits.org/en/v1.0.0/) to
your commit messages.
- Use gitflow workflow to create your branches. Work on your feature branch, and
  when ready, create a pull request to merge it into **develop** branch.
- Keep in mind the following structure for your code. All lessons should include
  at least the files below:
  - `src/<level>/<lesson>/<files.py>`: Include all files needed for the lesson.
    Remember to import them in `__init__.py` file.
  - `tests/<level>/<lesson>/<test_lesson.py>`: tests for the lesson. One file
    per lesson.
  - `docs/<level>/<lesson.md>`: documentation for the lesson. One file per
    lesson.
- Make sure to include the lesson in the corresponding level inside `mkdocs.yml`
  file, so it is visible in the documentation.
- Run tests and aim for 100% coverage. Run `make test` to run tests and
  check coverage.
- The project is configured to use [pre-commit](https://pre-commit.com/) to
  check Python and markdown files are following the style guide. pre-commit is
  automatically installed when running `make install`. Rules are defined in
  `.pre-commit-config.yaml` and include:
  - [markdownlint](https://github.com/igorshubovych/markdownlint-cli): markdown
    code linter.
  - [black](https://github.com/psf/black): Python code formatter.
  - [bandit](https://github.com/PyCQA/bandit): Python security linter.
  - [ruff](https://github.com/astral-sh/ruff-pre-commit): Python code linter.
  - [cspell](https://github.com/streetsidesoftware/cspell-cli): Spelling checker.
  - mkdocs-build: Local hook to make sure mkdocs build is working properly.
- Run `pre-commit run --all-files` to run all pre-commits checks for all files
  in the project, or `pre-commit run <hook_id>` to run a specific hook.
