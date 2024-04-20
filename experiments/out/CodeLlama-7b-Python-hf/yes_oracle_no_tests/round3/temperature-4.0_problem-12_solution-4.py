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
        return Non
    else:
        max_len = 0
        for i in strings:
            if len(i) > max_len:
                max_len = len(i)
        for j in strings:
            if len(j) == max_len:
                return j

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)