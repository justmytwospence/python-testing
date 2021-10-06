import doctest


def my_sum(*args):
    """
    >>> my_sum(1,2,3,4)
    10
    >>> my_sum(*[1,2], *[3,4], *[5,6])
    21
    """
    result = 0
    for arg in args:
        result += arg
    return result


def concatenate(**kwargs):
    """
    >>> concatenate(
    ...    a = "Real",
    ...    b = "Python",
    ...    c = "Is", 
    ...    d = "Great") 
    ('abcd', 'RealPythonIsGreat')
    >>> concatenate(
    ...    **{"a": "Real",
    ...       "b": "Python"},
    ...    **{"c": "Is",
    ...       "d": "Great"})
    ('abcd', 'RealPythonIsGreat')
    """
    keys = ""
    values = ""
    for key in kwargs:
        keys += key
    for value in kwargs.values():
        values += value
    return keys, values


if __name__ == "__main__":
    doctest.testmod()

