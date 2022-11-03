import doctest


def square(num: int):
    """
    :param num: int
    :return: int

    returns the square of the number

    >>> square(3)
    9
    """

    return num**2


doctest.testmod()
