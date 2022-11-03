import doctest


def top_three_avg(a: int, b: int, c: int, d: int) -> float:
    """
    Calculate average of top 3 grades

    :param a: int
    :param b: int
    :param c: int
    :param d: int
    :return: float

    >>> top_three_avg(50, 60, 70, 80)
    70.0
    """

    initial_values = [a, b, c, d]
    min_val = min(initial_values)
    new_values = [x for x in initial_values if x is not min_val]

    total = 0
    for i in new_values:
        total += i

    return total/3


top_three_avg(1, 2, 7, 4)

doctest.testmod()
