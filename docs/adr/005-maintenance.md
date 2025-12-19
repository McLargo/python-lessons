# ADR-005 - DependencyMaintenance

| Creation Date | Status   | Author                                 |
| :-----------: | :------: | :------------------------------------: |
| 19/12/2025    | Accepted | [@mclargo](https://github.com/McLargo) |

## Context and Problem Statement

Current situation is that project is not often updated. And when we want to run
it, sometimes we find out that some dependencies are not in the last version.
Usually, nothing is critical/or broken, but it's annoying and time-consuming to
update dependencies manually.

## Solution

We want to use a tool that automatically review my dependencies and creates pull
requests in my github repository to update dependencies in the project. List of
requirements for the tool:

- It should support poetry, github actions and pre-commit hooks.
- It should be free for open source projects.
- It should be easy to configure and maintain.

I explored Renovate Bot and it seems to fit our needs as it supports all the
requirements above described. I installed github app and created configuration
file inside my repository. Renovate Bot was automatically reviewing dependencies
and PRs started to appear with the updated dependencies.

I tuned configuration a bit to avoid too many PRs and to group some dependencies
together (except python and pre-commit hooks, which I want to update
separately).

Still in alpha stage of usage, but so far it looks promising and I hope it will
save me some time in the future.

## Other Solutions Considered

I used Dependabot in other project, but it didn't support pre-commit. But I do
remember that it was quite easy to use as well.
