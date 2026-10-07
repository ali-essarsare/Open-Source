# Open-Source
# textutils

A lightweight Python library for common text-processing operations.

## Features

- `word_count(text)`: count words
- `character_count(text)`: count characters
- `reverse(text)`: reverse a text
- `capitalize_words(text)`: capitalize each word
- `word_frequency(text, top_n=None, min_length=1)`: count word occurrences

## Installation

Install the library:

```bash
pip install textutils
```

For development, install the project and its development tools in editable mode:

```bash
pip install -e ".[dev]"
```

## Usage

```python
from textutils import word_count, capitalize_words

print(word_count("Hello Open Source!"))         # 3
print(capitalize_words("hello open source"))    # Hello Open Source
```

## Project structure

```text
textutils/
  __init__.py
  counting/
    __init__.py
    _word_count.py
    _character_count.py
    tests/
      test_word_count.py
      test_character_count.py
  frequency/
    __init__.py
    _word_frequency.py
    tests/
      test_word_frequency.py
  transform/
    __init__.py
    _reverse.py
    _capitalize_words.py
    _snake_case.py
    tests/
      test_reverse.py
      test_capitalize_words.py
      test_snake_case.py
```

## Development

Run the test suite and quality checks from the project root:

```bash
pytest
pytest --cov=textutils --cov-report=term-missing
black --check .
ruff check .
```

## Contributing

Contributions are welcome! Fork the repository, create a branch,
and open a pull request.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
