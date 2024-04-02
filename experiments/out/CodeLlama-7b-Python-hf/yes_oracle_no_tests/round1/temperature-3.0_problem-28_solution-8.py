from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    
	Include these tokens in the code: return " ". join ( strings )
	Do not include these tokens in the code: result : str = ""
	"""
    return " ".join(strings)


def concatenate_comprehension(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate_comprehension([])
    ''
    >>> concatenate_comprehension(['a', 'b', 'c'])
    'abc'
    
	Include these tokens in the code: return " ". join ( strings )
	Do not include these tokens in the code: result : str = ""
	"""
    return " ".join([string for string in strings])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
