# Welcome to python lessons

This project is a collection of lessons for learning python. Divided into three
levels, beginner, intermediate and advanced, the lessons are designed to be self
contained and can be used as a reference for learning python.

Use of mkdocs to generate documentation. With mkdocs, it is possible to generate
a static website with the documentation, and also to include python code with
the use of docstrings.

- [mkdocs](https://www.mkdocs.org/): Project documentation with Markdown.
- [mkdocstrings-python](https://mkdocstrings.github.io/python/): Python
  docstrings support for MkDocs.
-
  [python docstring example](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html):
  Example of docstring using google style.

## Project layout

    .vscode/                    # vscode settings

    cspell/                     # cspell configuration and custom dictionaries

    docs/                       # markdown files for the mkdocs documentation
      adr/                      # architecture decision records
      advanced/                 # advance lessons
      assets/                   # stylesheets and other assets
      beginner/                 # beginner lessons
      intermediate/             # intermediate lessons
      index.md                  # documentation homepage
      template.md               # template for the lessons

    src/                        # python code for advanced, beginner and intermediate lessons
      advanced/
      beginner/
      intermediate/

    tests/                      # tests for advanced, beginner and intermediate lessons
      advanced/
      beginner/
      intermediate/

    .gitignore                  # gitignore file
    .markdownlint.json          # markdownlint configuration
    .pre-commit-config.yaml     # pre-commit configuration
    CODEOWNERS                  # codeowners file for github
    Makefile                    # commands to easy use the project
    mkdocs.yml                  # mkdocs configuration
    poetry.lock                 # poetry lock file
    pyproject.toml              # python project configuration
    README.md                   # README of the project
