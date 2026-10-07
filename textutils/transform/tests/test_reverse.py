"""Tests for the public reverse transformation."""

import pytest

from textutils.transform import reverse


@pytest.mark.parametrize(
    "text, expected",
    [
        ("abc", "cba"),
        ("", ""),
        ("a", "a"),
        ("radar", "radar"),
        ("Hello World", "dlroW olleH"),
        ("  ab ", " ba  "),
        ("a\tb\n", "\nb\ta"),
        ("café", "éfac"),
    ],
)
def test_reverse(text, expected):
    assert reverse(text) == expected


def test_reverse_twice_returns_original():
    text = "Open Source"
    assert reverse(reverse(text)) == text


@pytest.mark.parametrize("text", [None, 42])
def test_reverse_rejects_non_strings(text):
    with pytest.raises(TypeError, match="text must be a string"):
        reverse(text)
