from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    
	Do not include these tokens in the code: if strings == [] :
	"""
    return "".join(strings)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
