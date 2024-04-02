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


def concatenate_with_spaces(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string with spaces between them
    >>> concatenate_with_spaces([])
    ''
    >>> concatenate_with_spaces(['a', 'b', 'c'])
    'a b c'
    
	Include these tokens in the code: return " ".join(strings)
	Do not include these tokens in the code: result : str = ""
	"""
    return " ".join(strings)


def concatenate_with_and(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string with "and" between them
    >>> concatenate_with_and([])
    ''
    >>> concatenate_with_and(['a', 'b', 'c'])
    'a, b and c'
    >>> concatenate_with_and(['a', 'b'])
    'a and b'
    
	Include these tokens in the code: return ", ".join(strings[:-1]) + " and " + strings[-1]
	Do not include these tokens in the code: result : str = ""
	"""
    if len(strings) > 1:
        return ", ".join(strings[:-1]) + " and " + strings[-1]
    return " and ".join(strings)


def concatenate_with_commas(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string with commas between them
    >>> concatenate_with_commas([])
    ''
    >>> concatenate_with_commas(['a', 'b', 'c'])
    'a, b, c'
    
	Include these tokens in the code: return ", ".join(strings)
	Do not include these tokens in the code: result : str = ""
	"""
    return ", ".join(strings)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
