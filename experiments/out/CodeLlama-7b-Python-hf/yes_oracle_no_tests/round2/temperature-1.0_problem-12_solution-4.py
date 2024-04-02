from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    
	Do not include these tokens in the code: _
	"""


    if not strings:
        return None

 
    max_len = len(max(strings, key=len))
    return max(filter(lambda x: len(x) == max_len, strings))


def count_substring(string: str, sub_string: str) -> int:
    """Out of a string and a substring, return the number of occurrences of the substring in the
    string. Consider overlapping occurrences.
    >>> count_substring('', '')
    0
    
    >>> count_substring('a', '')
    1
    
    >>> count_substring('a', 'a')
    1
    
    >>> count_substring('aaa', 'a')
    3

    >>> count_substring('aaab', 'b')
    1

    >>> count_substring('abab', 'ab')
    2
    
    >>> count_substring('aaaa', 'aa')
    3
    
    >>> count_substring('aaaa', 'aaa')
    2
    
    >>> count_substring('abababab', 'abab')
    1
    
    >>> count_substring('aaaa', 'aaaab')
    0
    
    >>> count_substring('aaaaa', 'aaa')
    3
    """

    if not string or not sub_string:
        return 0

    count = 0
    sub_string_length = len(sub_string)
    for i in range(len(string)):
        if string[i:i + sub_string_length] == sub_string:
            count += 1
    return count


def count_substring_optimized(string: str, sub_string: str) -> int:
    """Out of a string and a substring, return the number of occurrences of the substring in the
    string. Consider overlapping occurrences.
    >>> count_substring('', '')
    0

    >>> count_substring('a', '')
    1

    >>> count_substring('a', 'a')
    1

    >>> count_substring('aaa', 'a')
    3

    >>> count_substring('aaab', 'b')
    1

    >>>