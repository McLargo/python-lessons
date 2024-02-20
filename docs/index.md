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

    .vscode/
      settings.json             # vscode settings
    cspell/
      dictionaries/             # custom dictionaries
      cspell.json               # cspell configuration
    docs/
      adr/                      # architecture Decision Records
      advanced/                 # markdown for advanced lessons
      assets/                   # stylesheets and other assets
      beginner/                 # markdown for beginner lessons
      intermediate/             # markdown for intermediate lessons
      index.md                  # documentation homepage
      template.md               # template for the lessons
    src/
      advanced/                 # python code for advanced lessons
      beginner/                 # python code for beginner lessons
      intermediate/             # python code for intermediate lessons
    tests/
      advanced/                 # tests for advanced lessons
      beginner/                 # tests for beginner lessons
      intermediate/             # tests for intermediate lessons

    .gitignore                  # gitignore file
    .markdownlint.json          # markdownlint configuration
    .pre-commit-config.yaml     # pre-commit configuration
    CODEOWNERS                  # codeowners file for github
    Makefile                    # makefile for project
    mkdocs.yml                  # mkdocs configuration
    poetry.lock                 # poetry lock file
    pyproject.toml              # poetry configuration
    README.md                   # README for project
