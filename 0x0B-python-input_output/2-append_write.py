#!/usr/bin/python3

"""a function that appends a string at the
end of a text file (UTF8)."""


def append_write(filename="", text=""):
    """appends a string at the
end of a text file (UTF8).
    Args:
        filename(str):
        text(str):
    Returns the number of characters added:
    """
    with open("filename", mode="a", encoding="utf-8") as f:
        return (f.write(text))
