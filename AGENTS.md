# AI Agent Instructions for Python Lessons Project

## Project Overview

This is an **educational Python repository** designed to teach Python concepts
through practical examples organized into three difficulty levels:

- **Beginner**: Fundamental Python concepts (classes, dataclasses, type
  checking, etc.)
- **Intermediate**: More advanced topics (exceptions, inheritance, logging,
  generators, etc.)
- **Advanced**: Complex patterns and techniques (patterns, concurrency, etc.)

**Primary Goal**: Provide clear, accurate, and well-tested Python examples with
comprehensive documentation that learners can understand and practice with.

## Project Structure

```text
docs/              → Markdown documentation for lessons
  beginner/        → Beginner lesson docs
  intermediate/    → Intermediate lesson docs
  advanced/        → Advanced lesson docs
  adr/             → Architecture Decision Records
  plans/           → Spec-driven and improvement plans
  template.md      → Template for new lessons

src/               → Python source code examples
  beginner/        → Beginner code examples
  intermediate/    → Intermediate code examples
  advanced/        → Advanced code examples

tests/             → Test files (mirrors `src/` structure)
  beginner/        → Tests for beginner examples
  intermediate/    → Tests for intermediate examples
  advanced/        → Tests for advanced examples
```

## Technology Stack

- **Documentation**: mkdocs with material theme, mkdocstrings for Python
  docstring integration
- **Testing**: pytest, pytest-cov (100% coverage required)
- **Quality Tools**:
  - ruff (linting)
  - cspell (spelling)
  - pre-commit hooks
  - mutmut (mutation testing)
  - hypothesis (property-based testing)
- **Package Manager**: Poetry

## Quality Standards

### Code Quality

1. **100% Test Coverage**: Every function, class, and method must have tests
2. **Type Hints**: All functions should include proper type hints
3. **Docstrings**: Use Google-style docstrings for all public functions/classes
4. **PEP 8 Compliance**: Follow Python style guidelines (enforced by ruff)
5. **No Dead Code**: Remove unused imports, variables, or functions

### Documentation Quality

1. **Clarity**: Explanations should be clear and accessible to the target
   audience level
2. **Completeness**: Cover the concept thoroughly with examples and edge cases
3. **Accuracy**: Technical explanations must be factually correct
4. **Practical Examples**: Include real-world use cases, not just toy examples
5. **Progressive Complexity**: Start simple, then show more advanced usage

### Docstring Requirements

Use Google-style docstrings with:

- Brief one-line summary
- Detailed description (if needed)
- Args: with type and description
- Returns: with type and description
- Raises: document exceptions
- Examples: when helpful

Example:

```python
def example_function(param: str) -> int:
    """Brief description of what the function does.

    Longer description if needed to explain the concept,
    implementation details, or usage patterns.

    Args:
        param: Description of the parameter.

    Returns:
        Description of what is returned.

    Raises:
        ValueError: When the parameter is invalid.

    Examples:
        >>> example_function("test")
        4
    """
    return len(param)
```

## Review Criteria

When reviewing or creating content, check for:

### 1. Technical Accuracy (Weight: 35%)

- [ ] Code is syntactically correct and runs without errors
- [ ] Explanations are technically accurate
- [ ] No misleading or incorrect statements
- [ ] Best practices are demonstrated
- [ ] No anti-patterns or bad practices

### 2. Code Quality (Weight: 25%)

- [ ] 100% test coverage achieved
- [ ] Tests cover edge cases and error conditions
- [ ] Type hints are present and correct
- [ ] Docstrings follow Google style
- [ ] Code passes ruff linting
- [ ] No spelling errors (cspell)

### 3. Educational Value (Weight: 25%)

- [ ] Concept is explained clearly
- [ ] Examples are relevant and practical
- [ ] Appropriate for the target level (beginner/intermediate/advanced)
- [ ] Builds on previous concepts appropriately
- [ ] Includes common pitfalls or gotchas

### 4. Documentation (Weight: 15%)

- [ ] Markdown is well-formatted
- [ ] Code blocks are properly formatted
- [ ] Links work correctly
- [ ] Documentation renders correctly in mkdocs
- [ ] Proper use of headings and structure

## Scoring Guidelines

Use this rubric to score lessons from 0-10:

### Score 9-10: Excellent

- All review criteria met
- Goes beyond basics with insightful examples
- Clear, comprehensive documentation
- Tests include edge cases and use advanced testing techniques (hypothesis, parametrize)
- Code demonstrates Python best practices and idioms

### Score 7-8: Good

- Meets all essential review criteria
- Minor improvements possible in clarity or completeness
- Good test coverage with standard pytest patterns
- Documentation is clear and accurate

### Score 5-6: Acceptable

- Core concept is correct but needs refinement
- Missing some test cases or edge cases
- Documentation could be clearer or more complete
- May have minor style issues

### Score 3-4: Needs Work

- Technical inaccuracies present
- Incomplete test coverage (<100%)
- Documentation is unclear or confusing
- Code style issues

### Score 0-2: Unacceptable

- Major technical errors
- Little to no test coverage
- Missing or severely inadequate documentation
- Does not meet basic quality standards

## Common Tasks & Guidelines

### Creating a New Lesson

The user should always create a new lesson following these steps:

1. **Create markdown file** in `docs/<level>/<lesson_name>.md`
2. **Create Python module** in `src/<level>/<lesson_name>.py` with docstrings
3. **Link to source** in markdown using mkdocstrings syntax:

```mkdocs
::: src.<level>.<lesson_name>
    options:
      members:
        - function_name
        - ClassName
```

The agent can suggest code snippets and help with the docstring format and test
generation. Then, the agent should review the content lesson.

### Reviewing Content

1. **Read the code and documentation thoroughly**
2. **Run the tests**: Verify they pass and check coverage
3. **Check against review criteria**: Score each category
4. **Provide specific feedback**: Point to exact lines/issues
5. **Give overall score**: Use the 0-10 rubric

### Fixing Errors

1. **Identify the issue**: Technical error, test failure, style issue, etc.
2. **Fix the root cause**: Don't just patch symptoms
3. **Update tests**: Ensure tests cover the fix
4. **Update documentation**: If the fix changes behavior
5. **Verify**: Run tests, check coverage, preview docs

### Best Practices to Enforce

- **DRY Principle**: Don't repeat yourself in code or docs
- **KISS Principle**: Keep it simple and straightforward
- **Explicit is better than implicit**: Clear code over clever code
- **Pythonic idioms**: Use list comprehensions, context managers, etc. appropriately
- **Error handling**: Show proper exception handling
- **Logging over print**: Use logging module for output in examples
- **Type safety**: Use type hints and validate with type checkers

## Expected Behavior

When assisting with this project:

1. **Always check test coverage**: Run `make test` after code changes
2. **Verify documentation renders**: Use `make server` to preview
3. **Follow the template**: Use `docs/template.md` for new lessons
4. **Check ADRs**: Consult Architecture Decision Records for context on decisions
5. **Maintain consistency**: Follow patterns from existing lessons
6. **Consider the audience**: Match complexity to the lesson level
7. **Test edge cases**: Don't just test the happy path
8. **Update related files**: If changing code, update docs and tests
9. **Update Lesson Quality in Readme**: If a lesson is added or modified, update
   the quality review section in README.md

## Keywords for Context

When user asks about:

- "lesson", "tutorial", "example" → They want educational content
- "test", "coverage" → Must achieve 100% coverage
- "docs", "documentation" → Check mkdocs rendering
- "error", "bug", "issue" → Review against quality criteria
- "score", "rate", "evaluate" → Use the 0-10 rubric above
- "beginner", "intermediate", "advanced" → Consider appropriate complexity

## Quality Checklist

Before considering any lesson complete:

- [ ] Code runs without errors
- [ ] 100% test coverage achieved
- [ ] All functions/classes have Google-style docstrings
- [ ] Type hints are present and correct
- [ ] Ruff linting passes
- [ ] Spelling check passes (cspell)
- [ ] Documentation renders correctly in mkdocs
- [ ] Examples are practical and educational
- [ ] Appropriate difficulty level
- [ ] Tests cover edge cases and error conditions
- [ ] No TODO or FIXME comments remain
- [ ] ADRs followed for architectural decisions

---

**Remember**: This is an educational project. Prioritize clarity, accuracy, and
learning value above all else. Every example should teach something valuable and
be technically correct.
