import doctest

"""
PLAN IN ENGLISH

- take in the input as a list
- create a blank list `result` to hold 0, 0 as the initial value, and index
- loop through the enumerated list that has indexes and values
- compare the value with the current state of the result list (first index; 0)
- if the current iteration's value is bigger, assign it instead
- naturally, the last assignment will be the largest

"""


def max_index(nums: [int]) -> [int]:
    """
    Get the maximum value and its index and return it as [value, index]

    :param nums: [int]
    :return: [int]

    >>> max_index([4, 3, 2, 4, 3, 6, 1, 5])
    [6, 5]
    """

    result = [0, 0]

    for i, v in enumerate(nums):
        if v > result[0]:
            result = [v, i]
        else:
            continue

    return result


doctest.testmod()
