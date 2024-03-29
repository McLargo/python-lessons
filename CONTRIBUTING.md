# Contributions guidelines

This project is open to contributions. If you want to contribute, please read
the guidelines below.

## How to get started

The most important thing is to be familiar with the project and the structure of
it. If not, please feel free to clone the repository, read the
[documentation](./README.md) and play with the code.

## How to report a bug

If you find a bug, please open an issue in the
[issue tracker](https://github.com/McLargo/python-lessons/issues). Code owners
will review the issue and provide feedback to you.

## How to contribute with a new lesson

### Before adding a new lesson

Please make sure topic is not already (partially or fully) cover in one existing
lesson. Suggest topics that are relevant to the community, from patterns to
usage, avoiding content highly tight to business logic.

### Submit your lesson

Open a new [issue](https://github.com/McLargo/python-lessons/issues). Code
owners will review it, and decide to move forward/reject the application.

Use the following template to submit your request:

```md
# <Lesson name>

- Level: <Beginner, Intermediate, Advanced>
- Topics: <List of topics/concepts to cover in the lesson>
- Description: <Briefly describe the purpose of the lesson and your motivation>
- Time: <Estimated time to complete the lesson>
- References: <List of references, if any>
```

### Implementing a lesson

If the request is approved, you can start implementing the lesson. Some
guidelines/tips to follow:

1. Fork and clone the repository.

2. Checkout the branch associated to the issue. Once you have the branch, you
   can start implementing the lesson.

3. Make the necessary changes to the code and documentation. At least:
   1. Markdown documentation, in `docs/<level>/<lesson.md>`.
   2. Code related in `src/<level>/<lesson>/`. Include all files needed for the
      lesson. Remember to import them in `__init__.py` file.
   3. Tests to cover the code in `tests/<level>/<lesson>/`. One file per lesson.
   4. Link to the lesson in the `mkdocs.yaml` file, so it is visible in the
      navigation menu.

4. Run tests and aim for 100% coverage. Run `make test` and `make coverage` to
   run tests and check coverage.

5. Commit your changes to the branch. Use
   [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) for
   your commits message. No matter if you create several commits, push request
   will be squashed to the main branch with a single commit message.

6. Push your changes and create a pull request. Select your branch and provide a
   descriptive title and description for your pull request.

### Review process

The project maintainers will shortly review your pull request and provide
feedback. Make any necessary changes based on the feedback. Once your pull
request has been approved, it will be merged into the main repository.
Congratulations, you have successfully contributed to the project!
