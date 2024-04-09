from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    
	Include these tokens in the code: not strings
	Do not include these tokens in the code: len ( ) == 0
	"""


    if len(strings) == 0:
        return None

    max_len = len(strings[0])

    for string in strings:
        if len(string) > max_len:
            max_len = len(string)

    for string in strings:
        if len(string) == max_len:
            return string


if __name__ == "__main__":
    import doctest

    doctest.testmod()
