from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i] for i in range(1, len(string) + 1)]


def longest_prefix(string: str) -> str:
    """ Return longest prefix of the input string
    >>> longest_prefix('abc')
    'a'
    """
    return string[0]


def longest_proper_prefix(string: str) -> str:
    """ Return longest proper prefix of the input string
    >>> longest_proper_prefix('abc')
    'a'
    """
    return string[:-1]
