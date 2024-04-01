from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return "".join(strings)


def concatenate_using_for_loop(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate_using_for_loop([])
    ''
    >>> concatenate_using_for_loop(['a', 'b', 'c'])
    'abc'
    """
    result = ""
    for string in strings:
        result += string
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
