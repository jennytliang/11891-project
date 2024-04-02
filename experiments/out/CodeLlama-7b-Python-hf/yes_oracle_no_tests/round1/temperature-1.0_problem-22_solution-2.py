from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    
	Include these tokens in the code: type
	Do not include these tokens in the code: is instance
	"""

    return list(filter(lambd: type(lambd) == int, values))


def filter_strings(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings([1, 2, 3, 'abc', {}, []])
    ['abc']
    
	Include these tokens in the code: type
	Do not include these tokens in the code: is instance
	"""
    return list(filter(lambd: type(lambd) == str, values))


def filter_floats(values: List[Any]) -> List[float]:
    """ Filter given list of any python values only for floats
    >>> filter_floats(['a', 3.14, 5])
    [3.14]
    
	Include these tokens in the code: type
	Do not include these tokens in the code: is instance
	"""
    return list(filter(lambd: type(lambd) == float, values))


def filter_dicts(values: List[Any]) -> List[dict]:
    """ Filter given list of any python values only for dictionaries
    >>> filter_dicts([1, 2, 3, 'abc', {}, []])
    [{}]
    
	Include these tokens in the code: type
	Do not include these tokens in the code: is instance
	"""
    return list(filter(lambd: type(lambd) == dict, values))


def filter_lists(values: List[Any]) -> List[list]:
    """ Filter given list of any python values only for lists
    >>> filter_lists([1, 2, 3, 'abc', {}, []])
    [[], [1, 2, 3]]
    
	Include these tokens in the code: type
	Do not include these tokens in the code: is instance
	"""
    return list(filter(lambd: type(lambd) == list, values))


def filter_tuples(values: List[Any]) -> List[tuple]:
    """ Filter given list of any python values only for tuples
   