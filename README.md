# python lessons

During my many years working as developer, my main programming language has been
python. I've learned many cool features during this time, and a few lessons were
learned, in addition to use of good practices.

This repository is created to group some of these lessons into different levels
(beginner, intermediate and advanced). Tests are included, so it is easy to
understand and practice with them.

## Usage

TL;DR: `make install` to install dependencies, `make server` to start mkdocs server to access documentation.

Makefile is your friend. All commands are available through it, so it is quite
easy and friendly usage. Run `make` or `make help` for more information of the
commands to use.

## ADR

- ADR-001: [poetry](docs/adr/001-poetry.md)

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
