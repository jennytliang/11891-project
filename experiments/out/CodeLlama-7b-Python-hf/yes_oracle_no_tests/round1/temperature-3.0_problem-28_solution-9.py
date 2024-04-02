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


def concatenate_with_separator(strings: List[str], separator: str = ",") -> str:
    """ Concatenate list of strings into a single string with a separator between each string
	>>> concatenate_with_separator([])
	''
	>>> concatenate_with_separator(['a', 'b', 'c'])
	'a,b,c'
	>>> concatenate_with_separator(['a', 'b', 'c'], separator=';')
	'a;b;c'
	
	Include these tokens in the code: return separator.join ( strings )
	Do not include these tokens in the code: result : str = ""
	"""
    return separator.join(strings)


def concatenate_with_spaces(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string with spaces between each string
	>>> concatenate_with_spaces([])
	''
	>>> concatenate_with_spaces(['a', 'b', 'c'])
	'a b c'
	
	Include these tokens in the code: return " ".join ( strings )
	Do not include these tokens in the code: result : str = ""
	"""
    return " ".join(strings)


def concatenate_with_commas_and_spaces(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string with commas and spaces between each string
	>>> concatenate_with_commas_and_spaces([])
	''
	>>> concatenate_with_commas_and_spaces(['a', 'b', 'c'])
	'a, b, c'
	
	Include these tokens in the code: return ", ".join ( strings )
	Do not include these tokens in the code: result : str = ""
	"""
    return ", ".join(strings)


def concatenate_with_newlines(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string with newlines between each string
	>>> concatenate_with_