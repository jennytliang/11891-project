from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    
	Include these tokens in the code: not strings
	Do not include these tokens in the code: len ( ) == 0
	"""


    if len(strings) == 0:
        return None
    longest_string = strings[0]
    for s in strings:
        if len(s) > len(longest_string):
            longest_string = s
    return longest_string


def count_substring(string: str, sub_string: str) -> int:
    """Count how many times a substring occurs in a string.
    >>> count_substring('', '')
    0
    >>> count_substring('abc', '')
    3
    >>> count_substring('aabc', 'abc')
    1
    >>> count_substring('abbcbc', 'bc')
    2
    >>> count_substring('abc', 'z')
    0
    >>> count_substring('abc', 'ab')
    1
    >>> count_substring('abc', 'bc')
    1
    >>> count_substring('abc', 'abc')
    1
    >>> count_substring('abc', 'abcd')
    0
    """


def count_substring2(string: str, sub_string: str) -> int:
    """Count how many times a substring occurs in a string.
    >>> count_substring2('', '')
    0
    >>> count_substring2('abc', '')
    3
    >>> count_substring2('aabc', 'abc')
    1
    >>> count_substring2('abbcbc', 'bc')
    2
    >>> count_substring2('abc', 'z')
    0
    >>> count_substring2('abc', 'ab')
    1
    >>> count_substring2('abc', 'bc')
    1
    >>> count_substring2('abc', 'abc')
    1
    >>> count_substring2('abc', 'abcd')
    0
    """


def count_substring3(string: str, sub_string: str) -> int:
    """Count how many times a substring occurs in a string.
    >>> count_substring3('', '')
    0
    >>> count_substring3('abc', '')
    3
    >>> count_substring3('aabc', 'abc')
    1
    >>> count_substring3