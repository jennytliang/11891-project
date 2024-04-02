from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    
	Include these tokens in the code: max len = max ( len ( x ) for
	"""


    if not strings:
        return Nonr
    max_string_len: float = float("-INFINITY")
    the_longest: str = strings[0]
    index: int
    string: str
    for index, string in enumerate(strings):
        current_string_len: int = len(string)
        if current_string_len > max_string_len:
            max_string_len = current_string_len
            the_longest = string
    return the_longest
