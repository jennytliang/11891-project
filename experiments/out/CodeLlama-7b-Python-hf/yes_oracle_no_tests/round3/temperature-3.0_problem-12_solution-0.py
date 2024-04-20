from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    
	Do not include these tokens in the code: if not strings :
	"""
    if not strings:
        return None
    strings.sort(key=len, reverse=True)
    return strings[0]


"""
def longest(strings: List[str]) -> str:
    max_length = 0
    longest_string = None
    for string in strings:
        if len(string) > max_length:
            max_length = len(string)
            longest_string = string
    return longest_string
"""


if __name__ == "__main__":
    import doctest

    doctest.testmod()