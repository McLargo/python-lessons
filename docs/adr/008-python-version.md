# ADR-08 - Install Python version

| Creation Date | Status   | Author                                 |
| :-----------: | :------: | :------------------------------------: |
| 21/10/2026    | Accepted | [@mclargo](https://github.com/McLargo) |

## Context and Problem Statement

The project should always include the best tools to keep the code clean. For
Python, it is important to ensure that the correct version is installed and used
consistently across different development environments and CI/CD pipelines. When
possible, use the latest version available of Python (stable version. not beta).

## Solution

[uv](https://docs.astral.sh/uv/) not only offers library version management, but
also allows to install different
[version of Python](https://docs.astral.sh/uv/concepts/python-versions/)
locally, so poetry can use to ensure the project is running with the correct
Python version.

The python installation should be manage by a make command, so there is no need
to know the exact steps to install it manually.

## Other Solution Considered

- poetry: python version management is possible, but it is experimental and not
  as robust as using uv for managing Python versions.
- conda: it is the popular choice for managing Python environments, but it adds
  complexity and overhead compared to using uv.
