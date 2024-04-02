from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    
	Do not include these tokens in the code: r = " "
	"""
    r = ""
    for s in strings:
        r += s
    return r


if __name__ == "__main__":
    import doctest

    doctest.testmod()
