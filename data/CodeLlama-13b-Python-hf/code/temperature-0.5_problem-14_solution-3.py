from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i] for i in range(1, len(string) + 1)]


def longest_prefix(strings: List[str]) -> str:
    """ Return longest common prefix of the list of input strings
    >>> longest_prefix(['abcdef', 'abc', 'abcde'])
    'abc'
    """
    prefixes = set(strings[0])
    for string in strings:
        prefixes = prefixes.intersection(set(string))
    return "".join(prefixes)


def longest_common_prefix(strings: List[str]) -> str:
    """ Return longest common prefix of the list of input strings
    >>> longest_common_prefix(['abcdef', 'abc', 'abcde'])
    'abc'
    """
    prefixes = all_prefixes(strings[0])
    for string in strings:
        prefixes = [prefix for prefix in prefixes if string.startswith(prefix)]
    return prefixes[-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
