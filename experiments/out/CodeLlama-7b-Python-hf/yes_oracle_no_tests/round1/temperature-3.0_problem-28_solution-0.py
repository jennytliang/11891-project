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
    """ Concatenate list of strings into a single string with spaces in between
    >>> concatenate_with_spaces([])
    ''
    >>> concatenate_with_spaces(['a', 'b', 'c'])
    'a b c'
    
	Include these tokens in the code: return " ".join ( strings )
	Do not include these tokens in the code: result : str = ""
	"""
    return " ".join(strings)


def concatenate_with_commas(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string with commas in between
    >>> concatenate_with_commas([])
    ''
    >>> concatenate_with_commas(['a', 'b', 'c'])
    'a, b, c'
    
	Include these tokens in the code: return ", ".join ( strings )
	Do not include these tokens in the code: result : str = ""
	"""
    return ", ".join(strings)


def concatenate_with_commas_and_spaces(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string with commas and spaces in between
    >>> concatenate_with_commas_and_spaces([])
    ''
    >>> concatenate_with_commas_and_spaces(['a', 'b', 'c'])
    'a, b, c'
    
	Include these tokens in the code: return ", ".join ( strings )
	Do not include these tokens in the code: result : str = ""
	"""
    return ", ".join(strings)


def concatenate_with_newlines(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string with newlines in between
    >>> concatenate_with_newlines([])
    ''
    >>> concatenate_with_newlines(['a', 'b', 'c'])
    'a\nb\nc'
    
	Include these tokens in the code: return "\n".