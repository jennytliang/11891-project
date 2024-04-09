from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    
	Include these tokens in the code: ".
	"""

    ret_string = ''
    for string in strings:
        ret_string += string

    return ret_string


def concatenate_placement(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate_placement([])
    ''
    >>> concatenate_placement(['a', 'b', 'c'])
    'abc'
    
	Include these tokens in the code: ".
	"""

    ret_string = ''
    for string in strings:
        ret_string += ' ' + string

    return ret_string


def concatenate_plus(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate_plus([])
    ''
    >>> concatenate_plus(['a', 'b', 'c'])
    'abc'
    
	Include these tokens in the code: "+".
	"""

    ret_string = ''
    for string in strings:
        ret_string += string

    return ret_string


def concatenate_placement_plus(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate_placement_plus([])
    ''
    >>> concatenate_placement_plus(['a', 'b', 'c'])
    'abc'
    
	Include these tokens in the code: "+".
	"""

    ret_string = ''
    for string in strings:
        ret_string += ' ' + string

    return ret_string


def concatenate_join(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate_join([])
    ''
    >>> concatenate_join(['a', 'b', 'c'])
    'abc'
    
	Include these tokens in the code: ".join".
	"""

    ret_string = ''
    for string in strings:
        ret_string += string

    return ret_string


def concatenate_placement_join(strings: List[str