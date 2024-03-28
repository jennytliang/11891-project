from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i] for i in range(len(string) + 1)]


def all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_suffixes('abc')
    ['c', 'bc', 'abc']
    """
    return all_prefixes(string[::-1])[::-1]


def all_substrings(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings('abc')
    ['a', 'ab', 'abc', 'b', 'bc', 'c']
    """
    return all_prefixes(string) + all_suffixes(string)[1:]


def all_substrings_v2(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings_v2('abc')
    ['a', 'ab', 'abc', 'b', 'bc', 'c']
    """
    return [string[i:j + 1] for i in range(len(string)) for j in range(i, len(string))]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
