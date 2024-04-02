from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    
	Include these tokens in the code: if not strings :
	"""
    if len(strings) == 0:
        return None
    strings.sort(key=len, reverse=True)
    return strings[0]


print(longest([]))
print(longest(['a', 'b', 'c']))
print(longest(['a', 'bb', 'ccc']))
print(longest(['a', 'b', 'c', 'ddddd']))
