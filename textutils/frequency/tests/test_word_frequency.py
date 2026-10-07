"""Tests for the public word-frequency API."""

import pytest

from textutils.frequency import word_frequency


@pytest.mark.parametrize(
    "text, kwargs, expected",
    [
        (
            "the cat and the dog and the bird",
            {},
            [("the", 3), ("and", 2), ("bird", 1), ("cat", 1), ("dog", 1)],
        ),
        ("Hello, hello! HELLO?", {}, [("hello", 3)]),
        (
            "Don't stop: open-source is open-source",
            {"top_n": 2},
            [("open-source", 2), ("don't", 1)],
        ),
        (
            "a bb ccc bb ccc ccc",
            {"min_length": 2},
            [("ccc", 3), ("bb", 2)],
        ),
        ("", {}, []),
        ("   \t\n", {}, []),
        ("The cat", {"top_n": 0}, []),
        (
            "Le café est très bon, le café!",
            {},
            [("café", 2), ("le", 2), ("bon", 1), ("est", 1), ("très", 1)],
        ),
        ("wait -- what", {}, [("wait", 1), ("what", 1)]),
        ("'hello' hello", {}, [("hello", 2)]),
        ("hello,world", {}, [("hello", 1), ("world", 1)]),
        ("Hello", {}, [("hello", 1)]),
        ("hello hello", {"min_length": 6}, []),
    ],
)
def test_word_frequency(text, kwargs, expected):
    assert word_frequency(text, **kwargs) == expected


@pytest.mark.parametrize("text", [None, 42])
def test_word_frequency_rejects_non_strings(text):
    with pytest.raises(TypeError, match="text must be a string"):
        word_frequency(text)


def test_word_frequency_rejects_negative_top_n():
    with pytest.raises(ValueError, match="top_n must not be negative"):
        word_frequency("hi", top_n=-1)


def test_word_frequency_rejects_min_length_below_one():
    with pytest.raises(ValueError, match="min_length must be at least 1"):
        word_frequency("hi", min_length=0)
