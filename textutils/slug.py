"""URL-friendly slug generation."""

import re
import unicodedata

# Letters that do not decompose under NFKD but have a sensible ASCII form.
_SPECIAL = str.maketrans({
    "ß": "ss", "æ": "ae", "œ": "oe", "ø": "o", "đ": "d", "ł": "l", "þ": "th",
})

_WORD_RE = re.compile(r"[a-z0-9]+")


def slugify(text, separator="-", max_length=None):
    """Convert ``text`` into a URL-friendly slug.

    - Lowercases and strips accents (é -> e, ç -> c, ñ -> n).
    - Any run of non-alphanumeric characters becomes a single ``separator``.
    - No leading or trailing separator.
    - If ``max_length`` is given, the slug never exceeds it and is cut at a
      word boundary. If the first word alone is too long, it is truncated.

    Characters with no ASCII equivalent (e.g. CJK) are dropped.

    Raises:
        TypeError: if ``text`` or ``separator`` is not a string, or
            ``max_length`` is not an int.
        ValueError: if ``max_length`` is negative.
    """
    if not isinstance(text, str):
        raise TypeError(f"text must be a str, got {type(text).__name__}")
    if not isinstance(separator, str):
        raise TypeError(f"separator must be a str, got {type(separator).__name__}")
    if max_length is not None:
        if isinstance(max_length, bool) or not isinstance(max_length, int):
            raise TypeError("max_length must be an int or None")
        if max_length < 0:
            raise ValueError("max_length must be >= 0")

    text = text.lower().translate(_SPECIAL)
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    words = _WORD_RE.findall(text)

    if not words:
        return ""
    if max_length is None:
        return separator.join(words)

    result = words[0][:max_length]
    if len(words[0]) > max_length:
        return result
    for word in words[1:]:
        candidate = result + separator + word
        if len(candidate) > max_length:
            break
        result = candidate
    return result