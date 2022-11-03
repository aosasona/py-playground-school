import doctest


def km_to_miles(miles: int) -> float:
    """
    Convert km to miles

    :param miles: int
    :return: float

    >>> km_to_miles(5)
    3.125
    """
    return miles/1.6


doctest.testmod()
