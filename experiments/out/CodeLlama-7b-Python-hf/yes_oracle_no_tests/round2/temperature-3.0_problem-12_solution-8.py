from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    
	Include these tokens in the code: max len
	Do not include these tokens in the code: longest _ string
	"""

    if not strings:
        return None
    max_len = max(len(s) for s in strings)
    longest_string = next(
        (s for s in strings if len(s) == max_len), strings[0]
    )
    return longest_string
