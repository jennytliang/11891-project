from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    
	Include these tokens in the code: return list ( filter ( lambda x : type (
	"""
    return [x for x in values if isinstance(x, int)]


def filter_floats(values: List[Any]) -> List[float]:
    """ Filter given list of any python values only for floats
    >>> filter_floats([1, 2.2, 3.0, 'abc', {}, []])
    [2.2, 3.0]
    
	Include these tokens in the code: return list ( filter ( lambda x : type (
	"""
    return [x for x in values if isinstance(x, float)]


def filter_strings(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings([1, 2.2, 3.0, 'abc', {}, []])
    ['abc']
    
	Include these tokens in the code: return list ( filter ( lambda x : type (
	"""
    return [x for x in values if isinstance(x, str)]


def filter_dicts(values: List[Any]) -> List[dict]:
    """ Filter given list of any python values only for dictionaries
    >>> filter_dicts([1, 2.2, 3.0, 'abc', {}, []])
    [{}, {}]
    
	Include these tokens in the code: return list ( filter ( lambda x : type (
	"""
    return [x for x in values if isinstance(x, dict)]


def filter_lists(values: List[Any]) -> List[list]:
    """ Filter given list of any python values only for lists
    >>> filter_lists([1, 2.2, 3.0, 'abc', {}, []])
    [[], []]
    
	Include these tokens in the code: return list ( filter ( lambda x : type (
	"""
    return [x for x in values if isinstance(x, list)]


def filter_functions(values: List[Any]) -> List[list]:
    """ Filter given list of any python values only for functions
    >>> filter_functions([1, 2.2, 3.0,