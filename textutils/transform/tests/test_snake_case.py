"""Tests for the public snake_case transformation."""

import pytest

from textutils.transform import snake_case


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Hello World", "hello_world"),
        ("Hello    World", "hello_world"),
        ("  Hello Open Source  ", "hello_open_source"),
        ("Hello\tWorld\nAgain", "hello_world_again"),
        ("Hello", "hello"),
        ("", ""),
        ("   ", ""),
        ("hello_world", "hello_world"),
        ("café crème", "café_crème"),
        ("one  two", "one_two"),
    ],
)
def test_snake_case(text, expected):
    assert snake_case(text) == expected


@pytest.mark.parametrize("text", [None, 42])
def test_snake_case_rejects_non_strings(text):
    with pytest.raises(TypeError, match="text must be a string"):
        snake_case(text)
