"""Tests for the public word-counting API."""

import pytest

from textutils.counting import word_count


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Hello Open Source!", 3),
        ("Hello", 1),
        ("", 0),
        ("   ", 0),
        ("Hello    World", 2),
        ("  Hello World  ", 2),
        ("\t\n", 0),
        ("Hello\tWorld\nAgain", 3),
        ("café crème", 2),
        ("open-source is great", 3),
    ],
)
def test_word_count(text, expected):
    assert word_count(text) == expected


@pytest.mark.parametrize("text", [None, 42])
def test_word_count_rejects_non_strings(text):
    with pytest.raises(TypeError, match="text must be a string"):
        word_count(text)
