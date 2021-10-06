import doctest


def reverse_string_in_place(s):
    """
    >>> reverse_string_in_place("foobar")
    'raboof'
    """
    chars = list(s)
    for i in range(len(s) // 2):
        char = chars[i]
        chars[i] = chars[len(s) - 1 - i]
        chars[len(s) - 1 - i] = char
    return "".join(chars)


def reverse_string_copy(s):
    """
    >>> reverse_string_copy("foobar")
    'raboof'
    """
    chars = ""
    for char in s:
        chars = char + chars
    return chars


def reverse_string_recursive(s):
    """
    >>> reverse_string_recursive("foobar")
    'raboof'
    """
    if len(s) == 1: # base case
        return s
    else: # recursive case
        return reverse_string_recursive(s[1:]) + s[0]


if __name__ == "__main__":
    doctest.testmod()
    reverse_string_in_place("baz")
