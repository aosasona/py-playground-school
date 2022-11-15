import doctest

"""
accept input for a series of single-digit numbers with nothing separating them as string
create an initial sum of 0
loop through each character in the string
convert the character to an integer
add the integer to the sum
print the sum
"""


def take_input() -> str:
    return input("Enter a series of single-digit numbers with nothing separating them: ")


def sum_digits(number: str) -> int:
    """
    >>> sum_digits("123")
    6
    >>> sum_digits("12345")
    15
    """

    total = 0
    for i in number:
        total += int(i)
    return total


def main():
    number = take_input()
    print(sum_digits(number))


doctest.testmod().failed == 0 and main()  # execute only if the doctests pass
