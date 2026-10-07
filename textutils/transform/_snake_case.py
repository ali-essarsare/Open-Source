"""Convert whitespace-separated words to snake_case."""


def snake_case(text):
    """Convert a text to snake_case.

    The text is lowercased and its words, separated by any amount of
    whitespace, are joined with underscores. Leading and trailing
    whitespace is ignored.

    Parameters
    ----------
    text : str
        The text to convert.

    Returns
    -------
    str
        The snake_case version of ``text``.

    Raises
    ------
    TypeError
        If ``text`` is not a string.

    Examples
    --------
        >>> snake_case("Hello World")
        'hello_world'
        >>> snake_case("  Hello   Open  Source ")
        'hello_open_source'
        >>> snake_case("")
        ''
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return "_".join(text.lower().split())
