"""Count word occurrences in a string."""

import re
from collections import Counter


def word_frequency(text, top_n=None, min_length=1):
    """Count how many times each word appears in a text.

    Case-insensitive, punctuation ignored. Apostrophes and hyphens are
    only kept when inside a word (e.g. "don't", "open-source").
    Accented letters are kept.

    Parameters
    ----------
    text : str
        The input string.
    top_n : int, optional
        If given, return only the top_n most frequent words.
    min_length : int, default=1
        Minimum word length to include in the result.

    Returns
    -------
    list of tuple
        (word, count) tuples, sorted by count descending, then
        alphabetically for ties.

    Raises
    ------
    TypeError
        If text is not a string.
    ValueError
        If top_n is negative or min_length is less than 1.

    Examples
    --------
        >>> word_frequency("the cat and the dog and the bird")
        [('the', 3), ('and', 2), ('bird', 1), ('cat', 1), ('dog', 1)]
        >>> word_frequency("Don't stop: open-source is open-source", top_n=2)
        [('open-source', 2), ("don't", 1)]
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if top_n is not None and top_n < 0:
        raise ValueError("top_n must not be negative")
    if min_length < 1:
        raise ValueError("min_length must be at least 1")

    raw_words = re.findall(r"[^\W_]+(?:['’-][^\W_]+)*", text.lower())
    words = [word for word in raw_words if len(word) >= min_length]

    counts = Counter(words)
    result = sorted(counts.items(), key=lambda pair: (-pair[1], pair[0]))

    if top_n is not None:
        result = result[:top_n]

    return result
