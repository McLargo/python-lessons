# Docstring Standards

This document defines the docstring standards for the Python Lessons project.
All Python code must follow these standards to ensure consistency, clarity, and
proper integration with our documentation system (mkdocstrings).

## Why Docstrings Matter

Docstrings serve multiple purposes in this project:

1. **Documentation Generation**: They are automatically rendered in our mkdocs
   site via mkdocstrings
2. **Code Understanding**: They help learners understand the purpose and usage
   of functions/classes
3. **IDE Support**: They provide inline help in IDEs and editors
4. **Quality Assurance**: They ensure code is well-documented and maintainable

## Style Guide: Google-Style Docstrings

We use **Google-style docstrings** for all Python code. This style is:

- Clean and readable
- Well-supported by mkdocstrings
- Familiar to many Python developers
- Clear structure for arguments, returns, and exceptions

## Required Components

### For All Public Functions and Methods

Every public function and method MUST have:

1. **Brief Summary** (required): One-line description of what the function does
2. **Extended Description** (optional): Additional details if needed
3. **Args Section** (required if function has parameters): List all parameters
   with type and description
4. **Returns Section** (required if function returns a value): Describe the
   return value and its type
5. **Raises Section** (required if function raises exceptions): Document all
   exceptions that can be raised

### For All Public Classes

Every public class MUST have:

1. **Brief Summary** (required): One-line description of the class purpose
2. **Extended Description** (optional): Additional details about the class behavior
3. **Attributes Section** (required if class has public attributes): List all
   public attributes with type and description
4. **Examples Section** (optional): Usage examples can be helpful

### For Modules

Every module (`.py` file) MUST have:

1. **Module docstring**: Brief description of the module's purpose and contents
2. Place at the very top of the file (after any `#!/usr/bin/env python` shebang)

## Template Examples

### Function Docstring Template

```python
def example_function(param1: str, param2: int = 1) -> list[str]:
    """Brief one-line description of what the function does.

    Extended description providing more context about the function's
    behavior, algorithm, or any important implementation details.
    This section is optional but recommended for complex functions.

    Args:
        param1: Description of param1 and its purpose. Be specific
            about what values are expected.
        param2: Description of param2. Include information about
            default values when relevant. Defaults to 1.

    Returns:
        Description of what the function returns. Be specific about
        the structure and content of the return value.

    Raises:
        ValueError: When param2 is negative or zero.
        TypeError: When param1 is not a string.

    Examples:
        >>> example_function("hello", 2)
        ['hello', 'hello']
        >>> example_function("world")
        ['world']
    """
    if param2 <= 0:
        raise ValueError("param2 must be positive")
    return [param1] * param2
```

### Class Docstring Template

```python
class ExampleClass:
    """Brief one-line description of the class.

    Extended description explaining the purpose and behavior of the
    class. Describe what the class represents, when to use it, and
    any important patterns or conventions.

    Attributes:
        attribute1: Description of public attribute1.
        attribute2: Description of public attribute2.

    Examples:
        >>> obj = ExampleClass()
        >>> obj.do_something()
        'result'
    """

    def __init__(self, value: str) -> None:
        """Initialize ExampleClass.

        Args:
            value: Initial value for the instance.
        """
        self.attribute1 = value
        self.attribute2: list[str] = []

    def do_something(self) -> str:
        """Perform an action and return a result.

        Returns:
            A string describing the action performed.
        """
        return f"Processed: {self.attribute1}"
```

### Module Docstring Template

```python
"""Brief description of what this module provides.

This module demonstrates [concept] by providing practical examples
of [specific functionality]. It includes implementations of [key
classes/functions] that show [learning objectives].

Common use cases:
- Use case 1
- Use case 2
- Use case 3
"""

import sys
from typing import Any

# Rest of module code...
```

## Best Practices

### DO ✅

- **Be concise**: Keep the one-line summary under 80 characters
- **Be specific**: Use precise language that clearly describes behavior
- **Use active voice**: "Return the sum" not "The sum is returned"
- **Document types**: Include type information in Args and Returns sections
- **Document exceptions**: Always document exceptions that can be raised
- **Use proper grammar**: Start descriptions with capital letters, end with periods
- **Include examples**: Add examples for complex or non-obvious functions
- **Keep it current**: Update docstrings when you change function behavior

### DON'T ❌

- **Don't repeat the function signature**: The signature is already visible
- **Don't use vague descriptions**: Avoid "does stuff" or "handles things"
- **Don't document obvious parameters**: If `name: str` is clearly a person's
  name, brief is fine
- **Don't ignore exceptions**: If a function can raise an exception, document it
- **Don't use incorrect grammar**: Poor grammar makes documentation harder to
  read
- **Don't leave TODOs**: Finish documentation before committing code

## Type Hints vs. Docstrings

**Type hints and docstrings serve different purposes:**

- **Type hints**: Specify the types of parameters and return values
  (machine-readable)
- **Docstrings**: Explain what parameters mean and what the function does
  (human-readable)

**Both are required!**

```python
# GOOD: Type hints + descriptive docstring
def calculate_total(prices: list[float], tax_rate: float = 0.0) -> float:
    """Calculate the total price including tax.

    Args:
        prices: List of item prices before tax.
        tax_rate: Tax rate as a decimal (e.g., 0.08 for 8%). Defaults to 0.0.

    Returns:
        Total price including tax, rounded to 2 decimal places.
    """
    subtotal = sum(prices)
    return round(subtotal * (1 + tax_rate), 2)
```

## mkdocstrings Integration

Our documentation system uses mkdocstrings to automatically generate
documentation from docstrings.

### What Gets Displayed

When you use this in markdown:

```markdown
::: src.beginner.example
    options:
      members:
        - example_function
```

mkdocstrings will:

1. Extract the docstring from `example_function`
2. Render it with proper formatting
3. Include the function signature
4. Format Args, Returns, and Raises sections as structured lists
5. Syntax-highlight any code examples

### Private vs. Public Members

- **Public members** (no leading underscore): Automatically documented by
  mkdocstrings
- **Private members** (leading underscore): Hidden by default

```python
def public_function():
    """This will appear in documentation."""
    pass

def _private_function():
    """This will NOT appear unless explicitly included."""
    pass
```

## Examples Section (Optional)

Examples can be incredibly helpful, but they are **optional** for this project.
Include examples when:

- The function behavior is non-obvious
- There are common use cases worth demonstrating
- Edge cases need illustration

Use doctest format for examples:

```python
def greet(name: str, formal: bool = False) -> str:
    """Generate a greeting message.

    Args:
        name: Person's name to greet.
        formal: Whether to use formal greeting. Defaults to False.

    Returns:
        Greeting message string.

    Examples:
        >>> greet("Alice")
        'Hi Alice!'
        >>> greet("Dr. Smith", formal=True)
        'Good day, Dr. Smith.'
    """
    if formal:
        return f"Good day, {name}."
    return f"Hi {name}!"
```

## Common Mistakes to Avoid

### Mistake 1: Missing Extended Description for Complex Functions

```python
# BAD: One-liner insufficient for complex logic
def complex_calculation(data: list[int]) -> float:
    """Calculate result."""
    # ... 50 lines of complex logic ...

# GOOD: Extended description explains the algorithm
def complex_calculation(data: list[int]) -> float:
    """Calculate the weighted moving average of the input data.

    This function applies a triangular weighting scheme where more
    recent values have higher weights. The algorithm filters out
    outliers before calculating the average.

    Args:
        data: List of integer values to process.

    Returns:
        The weighted moving average as a float.
    """
    # ... 50 lines of complex logic ...
```

### Mistake 2: Not Documenting Default Behavior

```python
# BAD: Default value not explained
def fetch_data(limit: int = 100) -> list[dict]:
    """Fetch data from API.

    Args:
        limit: Number of records to fetch.

    Returns:
        List of data records.
    """

# GOOD: Default value explained
def fetch_data(limit: int = 100) -> list[dict]:
    """Fetch data from API.

    Args:
        limit: Maximum number of records to fetch. Defaults to 100,
            which is the API's maximum allowed value.

    Returns:
        List of data records as dictionaries.
    """
```

### Mistake 3: Missing Exception Documentation

```python
# BAD: No indication that function can raise exceptions
def divide(a: float, b: float) -> float:
    """Divide a by b."""
    return a / b

# GOOD: Exception documented
def divide(a: float, b: float) -> float:
    """Divide a by b.

    Args:
        a: Numerator.
        b: Denominator.

    Returns:
        Result of division.

    Raises:
        ZeroDivisionError: When b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
```

## Validation and Enforcement

### Pre-commit Hooks

Our pre-commit hooks include:

- **Ruff**: Checks for missing docstrings (pydocstyle rules)
- **Type checking**: Ensures type hints are present

### Code Review Checklist

When reviewing code, check:

- [ ] All public functions have docstrings
- [ ] All public classes have docstrings
- [ ] Module docstring is present
- [ ] Args section lists all parameters
- [ ] Returns section describes return value
- [ ] Raises section documents exceptions
- [ ] Docstrings use proper grammar and formatting
- [ ] Examples are included where helpful

## References

- [PEP 257 - Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)
- [Google Python Style Guide - Docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
- [mkdocstrings Documentation](https://mkdocstrings.github.io/)
- [Sphinx Napoleon - Google Style](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html#google-vs-numpy)

## Questions?

If you have questions about docstring standards:

1. Check this document first
2. Look at existing lessons for examples
3. Open an issue for clarification
4. Ask in pull request reviews

---

**Remember**: Good docstrings make the difference between code that's easy to
learn from and code that's frustrating to understand. Take the time to write
clear, comprehensive documentation!
