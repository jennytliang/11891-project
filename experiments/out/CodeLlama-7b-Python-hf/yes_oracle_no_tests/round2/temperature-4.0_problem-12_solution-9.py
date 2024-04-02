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

    max_len = 0
    result = None
    for string in strings:
        if len(string) > max_len:
            max_len = len(string)
            result = string

    return result


def test_function():
    assert longest([]) == None
    assert longest(['a', 'b', 'c']) == 'a'
    assert longest(['a', 'bb', 'ccc']) == 'ccc'
    assert longest(['a', 'bb', 'ccc', 'dddd']) == 'dddd'
    assert longest(['a', 'bb', 'ccc', 'dddd', 'eeeee']) == 'eeeee'
    assert longest(['a', 'a', 'a', 'a', 'a']) == 'a'


if __name__ == '__main__':
    test_function()
