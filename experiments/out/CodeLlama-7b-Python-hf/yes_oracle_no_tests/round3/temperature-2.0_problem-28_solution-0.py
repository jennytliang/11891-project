from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    
	Include these tokens in the code: ".
	"""

    ret = ''
    for string in strings:
        ret += string
    return ret


if __name__ == "__main__":
    import doctest
    doctest.testmod()

