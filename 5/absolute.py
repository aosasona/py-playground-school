import doctest


def absolute_difference(x: int, y: int) -> int:
    """
    Return the absolute value of the difference of two numbers

    :param x: int
    :param y: int
    :return: int

    >>> absolute_difference(5, 9)
    4
    """

    return abs((x - y))


doctest.testmod()
