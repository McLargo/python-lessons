# python lessons

During my many years working as developer, my main programming language has been
python. I've learned many cool features during this time, and a few lessons were
learned, in addition to use of good practices.

This repository is created to group some of these lessons into different levels
(beginner, intermediate and advanced). Tests are included, so it is easy to
understand and practice with them.

## Usage

TL;DR: `make install` to install dependencies, `make server` to start mkdocs
server to access documentation.

Makefile is your friend. All commands are available through it, so it is quite
easy and friendly usage. Run `make` or `make help` for more information of the
commands to use.

## ADR

- ADR-001: [poetry](docs/adr/001-poetry.md)
- ADR-002: [poetry](docs/adr/002-mkdocs.md)

## Contributing

Use [conventional commit](https://www.conventionalcommits.org/en/v1.0.0/) to
your commit messages.

Use gitflow workflow to create your branches. Work on your feature branch, and
when ready, create a pull request to merge it into **develop** branch.

Keep in mind following structure for your code. All lessons should include at
least files below:

- `src/<level>/<lesson>/<files.py>`: Include all files needed for the lesson.
  Remember to import them in `__init__.py` file.
- `tests/<level>/<lesson>/<test_lesson.py>`: tests for the lesson. One file per
  lesson.
- `docs/<level>/<lesson.md>`: documentation for the lesson. One file per lesson.

Make sure to include the lesson in `mkdocs.yml` file, so it is included in the
documentation, in the corresponding level.

Run always tests and aim for a 100% coverage. Run `make test` to run tests and
check coverage.

Project is configured to use [pre-commit](https://pre-commit.com/) to check
python and markdown code to follow the style guide. It should be automatically
installed when running `make install`. In case is not installed, run
`pre-commit install` to install it. Run `pre-commit run --all-files` to run
entire all checks in the entire project. Rules are defined in
`.pre-commit-config.yaml` and includes:

- markdownlint: markdown code linter
- black: python code formatter
- bandit: security linter
- ruff: python code linter
