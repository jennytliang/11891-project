from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    
	Include these tokens in the code: return " ". join ( strings )
	"""
    return " ".join(strings)


def concatenate_space(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate_space([])
    ''
    >>> concatenate_space(['a', 'b', 'c'])
    'a b c'
    
	Include these tokens in the code: return " ". join ( strings )
	"""
    return " ".join(strings)


def concatenate_comma(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate_comma([])
    ''
    >>> concatenate_comma(['a', 'b', 'c'])
    'a, b, c'
    
	Include these tokens in the code: return ", ". join ( strings )
	"""
    return ", ".join(strings)


def concatenate_dot(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate_dot([])
    ''
    >>> concatenate_dot(['a', 'b', 'c'])
    'a. b. c'
    
	Include these tokens in the code: return ". ". join ( strings )
	"""
    return ". ".join(strings)


def concatenate_hyphen(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate_hyphen([])
    ''
    >>> concatenate_hyphen(['a', 'b', 'c'])
    'a-b-c'
    
	Include these tokens in the code: return "-". join ( strings )
	"""
    return "-".join(strings)


def concatenate_colon(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate_colon([])
    ''
    >>> concatenate_colon(['a', 'b', 'c'])
    'a: b: c'
    
	Include these tokens in the code: return ": ". join ( strings )
	"""
   