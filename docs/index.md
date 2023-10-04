# Welcome to python lessons

This project is a collection of lessons for learning python. Divided into three levels, beginner, intermediate and advanced, the lessons are designed to be self contained and can be used as a reference for learning python.

Use of mkdocs to generate documentation. With mkdocs, it is possible to generate a static website with the documentation, and also to include python code with the use of docstrings.

- [mkdocs](https://www.mkdocs.org/): Project documentation with Markdown.
- [mkdocstrings-python](https://mkdocstrings.github.io/python/): Python docstrings support for MkDocs.
- [python docstring example](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html): Example of docstring using google style.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        adr/      # Architecture Decision Records
        advanced/ # Advanced lessons
        beginner/ # Beginner lessons
        intermediate/ # Intermediate lessons
    src/
        advanced/ # Python code for advanced lessons
        beginner/ # Python code for beginner lessons
        intermediate/ # Python code for intermediate lessons
    tests/
        advanced/ # tests for advanced lessons
        beginner/ # tests for beginner lessons
        intermediate/ # tests for intermediate lessons
