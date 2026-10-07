"""Count characters in a string."""


def character_count(text: str) -> int:
    """Count the characters in a text, including spaces and punctuation.

    Parameters
    ----------
    text : str
        The text whose characters are counted.

    Returns
    -------
    int
        The number of characters in ``text``.

    Raises
    ------
    TypeError
        If ``text`` is not a string.

    Examples
    --------
        >>> character_count("Hello")
        5
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return len(text)
