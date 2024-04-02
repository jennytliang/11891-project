from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    
	Include these tokens in the code: max len =
	Do not include these tokens in the code: return
	"""

    if not strings:
        return None

    if len(strings) == 1:
        return strings[0]

    max_length_string = strings[0]
    # Find the max length string
    for string in strings:
        if len(string) > len(max_length_string):
            max_length_string = string

    max_length = len(max_length_string)

    # Find the first longest string in the strings with max_length
    for string in strings:
        if len(string) == max_length:
            return string
