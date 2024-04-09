from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    
	Do not include these tokens in the code: max _ len = 0
	"""


    if not strings:
        return None
    else:
        max_len = 0
        max_str = strings[0]
        for string in strings:
            string_len = len(string)
            if string_len > max_len:
                max_len = string_len
                max_str = string
    return max_str


def longest_2(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    
	Do not include these tokens in the code: max _ len = 0
	"""


    if not strings:
        return None
    else:
        max_len = 0
        max_str = strings[0]
        for string in strings:
            string_len = len(string)
            if string_len > max_len:
                max_len = string_len
                max_str = string
    return max_str


def longest_3(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    
	Do not include these tokens in the code: max _ len = 0
	"""


    if not strings:
        return None
    else:
        max_len = 0
        max_str = strings[0]
        for string in strings:
            string_len = len(string)
            if string_len > max_len:
                max_len = string_len
                max_str = string
    return max_str


def longest_4(strings