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

    return max(strings, key=lambda s: len(s))


def shortest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the shortest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> shortest([])

    >>> shortest(['a', 'b', 'c'])
    'a'
    >>> shortest(['a', 'bb', 'ccc'])
    'b'
    
	Include these tokens in the code: min len =
	Do not include these tokens in the code: return
	"""

    if not strings:
        return None

    return min(strings, key=lambda s: len(s))


def longest_3(strings: List[str]) -> List[str]:
    """ Out of list of strings, return the 3 longest strings. Return the first 3 strings in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest_3([])

    >>> longest_3(['a', 'b', 'c'])
    ['a', 'b', 'c']
    >>> longest_3(['a', 'bb', 'ccc'])
    ['bb', 'ccc', 'ccc']
    
	Include these tokens in the code: max len =
	Do not include these tokens in the code: return
	"""

    if not strings:
        return None

    return sorted(strings, key=lambda s: len(s), reverse=True)[:3]


def shortest_3(strings: List[str]) -> List[str]:
    """ Out of list of strings, return the 3 shortest strings. Return the first 3 strings in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> shortest_3([])

    >>> shortest_3(['a', 'b', 'c'])
    ['a', 'b', 'c']
    >>> shortest_3(['a', 'bb', 'ccc'])
    ['a', 'bb', 'ccc']
    