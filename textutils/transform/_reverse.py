"""Reverse the characters in a string."""


def reverse(text: str) -> str:
    """Reverse a text.

    Parameters
    ----------
    text : str
        The text to reverse.

    Returns
    -------
    str
        The characters of ``text`` in reverse order.

    Raises
    ------
    TypeError
        If ``text`` is not a string.

    Examples
    --------
        >>> reverse("abc")
        'cba'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return text[::-1]
