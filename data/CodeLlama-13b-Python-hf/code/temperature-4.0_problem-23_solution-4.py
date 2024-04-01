def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    result = 0
    for symbol in string:
        result = result + 1
    return result
# print(strlen('abcde22f3'))


def strcmp(string1: str, string2: str) -> int:
    if (string1 == string2):
        return 0