"""Capitalize words in a string while preserving spaces."""


def capitalize_words(text: str) -> str:
    """Capitalize each space-separated word in a text.

    Parameters
    ----------
    text : str
        The text whose words are capitalized.

    Returns
    -------
    str
        The text with each space-separated word capitalized.

    Raises
    ------
    TypeError
        If ``text`` is not a string.

    Examples
    --------
        >>> capitalize_words("hello open source")
        'Hello Open Source'
        >>> capitalize_words("hello  world")
        'Hello  World'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return " ".join(word.capitalize() for word in text.split(" "))
