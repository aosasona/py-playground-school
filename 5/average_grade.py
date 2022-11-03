import doctest


def average_grade(x: int, y: int, z: int) -> float:
    """
    Calculate the average grade

    :param x: int
    :param y: int
    :param z: int
    :return: float

    >>> average_grade(2, 4, 6)
    4.0
    """

    # EXTRA TYPECHECKING FOR THE FUN
    for i in [x, y, z]:
        if type(i) is not int or 0 > i > 100:
            raise Exception("WTF!")
        break

    avg = (x + y + z)/3
    return avg


doctest.testmod()
