from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    result: str = ""

    for string in strings:
        result += string

    return result


print(concatenate(['a', 'b', 'c']))