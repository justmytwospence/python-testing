import doctest


class A():
    def __init__(self) -> None:
        print('A')
        super().__init__()


class B(A):
    def __init__(self) -> None:
        print('B')
        super().__init__()


class X():
    def __init__(self) -> None:
        print('X')
        super().__init__()


class Forward(B, X):
    """
    >>> forward = Forward()
    Forward
    B
    A
    X
    """

    def __init__(self) -> None:
        print('Forward')
        super().__init__()


class Backward(X, B):
    """
    >>> backward = Backward()
    Backward
    X
    B
    A
    """

    def __init__(self) -> None:
        print('Backward')
        super().__init__()


if __name__ == "__main__":
    doctest.testmod()
