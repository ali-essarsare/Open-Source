"""Tests for the public character-counting API."""

import pytest

from textutils.counting import character_count


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Hello", 5),
        ("", 0),
        ("Hello World", 11),
        ("   ", 3),
        ("  a  ", 5),
        ("a", 1),
        ("a\tb\n", 4),
        ("café", 4),
    ],
)
def test_character_count(text, expected):
    assert character_count(text) == expected


@pytest.mark.parametrize("text", [None, 42])
def test_character_count_rejects_non_strings(text):
    with pytest.raises(TypeError, match="text must be a string"):
        character_count(text)
