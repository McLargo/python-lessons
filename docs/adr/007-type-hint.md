# ADR-007 - Type Hint

| Creation Date | Status   | Author                                 |
| :-----------: | :------: | :------------------------------------: |
| 22/09/2026    | Accepted | [@mclargo](https://github.com/McLargo) |

## Context and Problem Statement

The project should always include the best tools to keep the code clean. For
python type hints are not mandatory, but recommended. Also, review which tools
can review the code and ensure type hints is added consistently in the code.

## Solution

[Pyrefly](https://pyrefly.org) is a type checked made in python. It is fast in
compare to other tools like mypy, and it provides pre-commit and github actions
integration, which are currently used in this project. Not only validates for
type hints, but also ensure there Python code is correctly working, catching
potential errors early in the development process, like methods not found,
methods being called with incorrect arguments or return types not matching the
expected type.

## Other Solution Considered

- mypy: it has been considered as a type checking tool for Python, as it is widely
  used in many Python projects. But performance wise is slower and configuration
  is not straightforward.
