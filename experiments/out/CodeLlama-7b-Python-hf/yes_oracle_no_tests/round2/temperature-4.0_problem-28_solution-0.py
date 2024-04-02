from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    
	Do not include these tokens in the code: #
	"""

    result = ''
    for s in strings:
        result += s
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
