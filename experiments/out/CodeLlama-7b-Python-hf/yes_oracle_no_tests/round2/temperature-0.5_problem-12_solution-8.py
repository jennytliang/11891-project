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
	Do not include these tokens in the code: r v
	"""


    if not strings:
        return Non
    else:
        return max(strings, key=len)


def shortest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the shortest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> shortest([])

    >>> shortest(['a', 'b', 'c'])
    'a'
    >>> shortest(['a', 'bb', 'ccc'])
    'b'
    
	Include these tokens in the code: min len
	Do not include these tokens in the code: r v
	"""


    if not strings:
        return None
    else:
        return min(strings, key=len)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
