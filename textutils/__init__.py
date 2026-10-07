"""Public API for the textutils package."""

from textutils.counting import character_count, word_count
from textutils.frequency import word_frequency
from textutils.transform import capitalize_words, reverse, snake_case

__all__ = [
    "capitalize_words",
    "character_count",
    "reverse",
    "snake_case",
    "word_count",
    "word_frequency",
]
