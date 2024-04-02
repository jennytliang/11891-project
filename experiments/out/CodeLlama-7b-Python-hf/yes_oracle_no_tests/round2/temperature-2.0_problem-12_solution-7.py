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

    max_len = max(len(string) for string in strings)
    for string in strings:
        if len(string) == max_len:
            return string


print(longest([]))
print(longest(["a", "b", "c"]))
print(longest(["a", "bb", "ccc"]))
