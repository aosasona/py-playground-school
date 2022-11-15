import doctest


def check_educational_email(email: str) -> bool:
    """
    >>> check_educational_email("test@gmail.com")
    False
    >>> check_educational_email("test@northampton.ac.uk")
    True
    """

    if email.endswith(".ac.uk"):
        return True
    else:
        return False


doctest.testmod()

# Test cases
print(check_educational_email("test@mail.com"))
print(check_educational_email("test@northampton.ac.uk"))
