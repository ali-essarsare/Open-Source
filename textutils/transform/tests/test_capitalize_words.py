"""Tests for the public capitalize_words transformation."""

import pytest

from textutils.transform import capitalize_words


@pytest.mark.parametrize(
    "text, expected",
    [
        ("hello open source", "Hello Open Source"),
        ("hello", "Hello"),
        ("", ""),
        ("Hello World", "Hello World"),
        ("hELLO wORLD", "Hello World"),
        ("HELLO WORLD", "Hello World"),
        ("don't stop", "Don't Stop"),
        ("élève à l'école", "Élève À L'école"),
        ("hello  world", "Hello  World"),
        (" hello ", " Hello "),
        ("  ", "  "),
        ("hello\tWORLD\nagain", "Hello\tworld\nagain"),
    ],
)
def test_capitalize_words(text, expected):
    assert capitalize_words(text) == expected


@pytest.mark.parametrize("text", [None, 42])
def test_capitalize_words_rejects_non_strings(text):
    with pytest.raises(TypeError, match="text must be a string"):
        capitalize_words(text)
