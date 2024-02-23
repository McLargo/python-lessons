# ADR-002 - mkdocs

| Creation Date | Status   | Author                                 |
| :-----------: | :------: | :------------------------------------: |
| 04/10/2023    | Accepted | [@mclargo](https://github.com/McLargo) |

## Context and Problem Statement

Goal is to create a live documentation for the python lessons, and also to
include python code, visible in the documentation automatically if there are any
changes. Also, all python code should be tested (tests not included in the
documentation at the moment).

## Solution

mkdocs provides a good solution for the problem. It is possible to generate a
documentation website with markdown files (lightweight markup language for
creating formatted text using a plain-text and simple format) and also to
include python code with the use of docstrings
([mkdocstrings-python](https://mkdocstrings.github.io/python/) library).

Additionally, we are adding
[mkdocs-material](https://squidfunk.github.io/mkdocs-material/) library. Not
only provides a nice theme. It also provides a lot of features and
customization, like search, footer and header customization, icons, annotation
and more. Feel free to check the documentation and see all the features, adding
those to the documentation if needed.

## Other Solution Considered

- pydocs: python documentation generator. It is a good tool, but it is not
  possible to include python code in the documentation.
- Jupyter Notebook: it is possible to include python code in the documentation,
  and execute live, but it is not possible to generate a static website with the
  documentation. Also, requires a lot of dependencies to be installed.
