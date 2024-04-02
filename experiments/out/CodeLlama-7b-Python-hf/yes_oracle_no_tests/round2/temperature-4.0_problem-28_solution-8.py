from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    
	Include these tokens in the code: return " ". join
	Do not include these tokens in the code: if len
	"""
    return " ".join(strings)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
