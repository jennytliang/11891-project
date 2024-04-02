from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    
	Include these tokens in the code: [ :(
	Do not include these tokens in the code: [:
	"""

    return [s for s in string[:i] for i in range(len(string) + 1)]


def longest_prefix(string: str) -> str:
    """ Return the longest prefix of the input string
    >>> longest_prefix('abc')
    'abc'
    >>> longest_prefix('ababc')
    'ab'
    """
    if not string:
        return string
    return max(all_prefixes(string), key=len)


def common_prefix(strings: List[str]) -> str:
    """ Return the longest prefix of the input strings
    >>> common_prefix(['abab', 'ababa'])
    'ab'
    >>> common_prefix(['abab', 'abac'])
    'aba'
    """
    if not strings:
        return ''
    return longest_prefix(min(strings, key=len))


def common_prefix_length(strings: List[str]) -> int:
    """ Return the length of the longest prefix of the input strings
    >>> common_prefix_length(['abab', 'abac'])
    3
    """
    if not strings:
        return 0
    return len(longest_prefix(min(strings, key=len)))


def common_prefix_weights(strings: List[str]) -> List[float]:
    """ Return the length of the longest prefix of the input strings
    >>> common_prefix_weights(['abab', 'abac'])
    [0.8, 0.8]
    """
    if not strings:
        return []
    common_prefix_length = len(longest_prefix(min(strings, key=len)))
    return [float(len(s)) / common_prefix_length for s in strings]
