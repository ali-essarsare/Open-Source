import pytest

from textutils import slugify


@pytest.mark.parametrize("text, kwargs, expected", [
    ("Hello World", {}, "hello-world"),
    (" Élève à l'école !! ", {}, "eleve-a-l-ecole"),
    ("Open_Source -- Rocks", {"separator": "_"}, "open_source_rocks"),
    ("Collaborative development with Git", {"max_length": 20}, "collaborative"),
    ("", {}, ""),
    ("!!!", {}, ""),
    ("ça va, señor?", {}, "ca-va-senor"),
    ("a   b\t\nc", {}, "a-b-c"),
    ("--leading and trailing--", {}, "leading-and-trailing"),
    ("snake_case_text", {}, "snake-case-text"),
    ("Python 3.12 released", {}, "python-3-12-released"),
    ("Straße", {}, "strasse"),
    ("日本語", {}, ""),
    ("a b", {"separator": ""}, "ab"),
    ("hello world", {"separator": "--"}, "hello--world"),
])
def test_basic(text, kwargs, expected):
    assert slugify(text, **kwargs) == expected


@pytest.mark.parametrize("text, max_length, expected", [
    ("hello world", 11, "hello-world"),
    ("hello world", 10, "hello"),
    ("hello world", 6, "hello"),
    ("supercalifragilistic is long", 5, "super"),
    ("hello world", 0, ""),
    ("a b c d", 3, "a-b"),
    ("hello world", 100, "hello-world"),
])
def test_max_length(text, max_length, expected):
    result = slugify(text, max_length=max_length)
    assert result == expected
    assert len(result) <= max_length


def test_max_length_with_custom_separator():
    assert slugify("one two three", separator="__", max_length=10) == "one__two"


@pytest.mark.parametrize("bad", [42, None, b"bytes", ["a"], 3.5])
def test_non_string_raises_type_error(bad):
    with pytest.raises(TypeError):
        slugify(bad)


def test_invalid_separator_and_max_length():
    with pytest.raises(TypeError):
        slugify("a", separator=1)
    with pytest.raises(TypeError):
        slugify("a", max_length="5")
    with pytest.raises(ValueError):
        slugify("a", max_length=-1)