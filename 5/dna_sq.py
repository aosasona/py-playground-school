import doctest


def find_value(val: str):
    dna_map = [["A", "T"], ["C", "G"]]
    for main in dna_map:
        for key, value in enumerate(main):
            if value is val:
                match key:
                    case 0:
                        return main[1]
                    case 1:
                        return main[0]
                    case _:
                        return None


def complement(dna: str) -> str:
    """
    Find DNA sequence complement

    :param dna: str
    :return: str

    >>> complement('AATTGCCGT')
    'TTAACGGCA'
    """

    res = ""
    for char in dna:
        complement_val = find_value(char)
        if complement_val is not None:
            res += complement_val
        else:
            res += char
    return res


doctest.testmod()
