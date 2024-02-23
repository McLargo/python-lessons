# ADR-004 - CI/CD Deployment

| Creation Date | Status   | Author                                 |
| :-----------: | :------: | :------------------------------------: |
| 23/02/2024    | Accepted | [@mclargo](https://github.com/McLargo) |

## Context and Problem Statement

Python lessons is a project build not only for the code owners, but also for the
community. These lessons can serve as reference, and inspire others. Who knows,
maybe someone will want to contribute to the project in the future.

We want to public our documentation in a production environment. This process
should be automated, once the documentation is merged to the main branch in the
repository. to automate the process of deploying the code to the production
environment.

## Solution

As we are using github to store our repository, the simplest solution is to use
GitHub Actions to automate the process of deploying the documentation to github
pages.

[material](https://squidfunk.github.io/mkdocs-material/publishing-your-site/#github-pages)
provides the corresponding github action to deploy the documentation to github
pages. To automate the process, we just need create a new workflow file in the
`.github/workflows`. Once the documentation is merged to the main branch, the
documentation should be available in the production environment shortly.

Locally, you can use `make deploy` to manually deploy the documentation to
github pages.

## Other Solutions Considered

None
