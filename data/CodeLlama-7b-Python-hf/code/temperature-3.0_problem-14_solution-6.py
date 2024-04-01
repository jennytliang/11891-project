from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """

    prefixes = []

    for index in range(len(string)):
        prefixes.append(string[: index + 1])

    return prefixes


def find_pattern(text: str, pattern: str) -> List[int]:
    """ Return indices of all occurrences of <pattern> in <text>

    Example:
        >>> find_pattern('abracadabra', 'abr')
        [0, 8]

    Note: O(m * n) time, O(1) space

    Where:
        m is length of <text>
        n is length of <pattern>
    """

    if len(pattern) == 0:
        return [0]

    indices = []
    for index in range(len(text) - len(pattern) + 1):
        if text[index : index + len(pattern)] == pattern:
            indices.append(index)
    return indices