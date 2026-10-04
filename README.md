# Open-Source
# textutils

A lightweight Python library for common text-processing operations.

## Features

- `word_count(text)`: count words
- `character_count(text)`: count characters
- `reverse(text)`: reverse a text
- `capitalize_words(text)`: capitalize each word
- `word_frequency(text, top_n=None, min_length=1)`: count word 
occurrences
- `slugify(text, separator="-", max_length=None)`: generate URL-friendly slugs

## Installation

```bash
pip install textutils
```

## Usage

```python
from textutils import word_count, capitalize_words

print(word_count("Hello Open Source!"))         # 3
print(capitalize_words("hello open source"))    # Hello Open Source
```

## Contributing

Contributions are welcome! Fork the repository, create a branch,
and open a pull request.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
