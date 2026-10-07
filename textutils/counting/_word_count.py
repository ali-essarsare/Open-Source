"""Count whitespace-separated words in a string."""


def word_count(text: str) -> int:
    """Count whitespace-separated words in a text.

    Parameters
    ----------
    text : str
        The text whose words are counted.

    Returns
    -------
    int
        The number of words in ``text``.

    Raises
    ------
    TypeError
        If ``text`` is not a string.

    Examples
    --------
        >>> word_count("Hello Open Source!")
        3
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return len(text.split())
