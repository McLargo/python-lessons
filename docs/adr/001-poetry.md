# ADR-001 - poetry installation

| Creation Date | Status   | Author                                 |
| :-----------: | :------: | :------------------------------------: |
| 04/10/2023    | Accepted | [@mclargo](https://github.com/McLargo) |

## Context and Problem Statement

This project is mean to be a collaborative project, and it is important to have
a properly configured environment, so everyone can run the project without any
issues or inconsistencies.

## Solution

In order to have a clean environment for this project, and to avoid issues with
different versions of libraries and other dependencies, I am going to use poetry.

Poetry helps to keep dependencies in one place, in a separated virtual
environment. As it uses pyproject.toml to keep the versions of the libraries, it
is easy to install and keep track of the dependencies.

## Other Solutions Considered

None
