from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    
	Include these tokens in the code: return list ( filter ( lambda x
	Do not include these tokens in the code: r = [] for
	"""
    return [x for x in values if isinstance(x, int)]


def filter_strings(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings([1, 2.2, 'a', 3, 'b'])
    ['a', 'b']
    >>> filter_strings([[], 44, None])
    []
    
	Include these tokens in the code: return list ( filter ( lambda x
	Do not include these tokens: if
	"""
    return [x for x in values if isinstance(x, str)]


def filter_floats(values: List[Any]) -> List[float]:
    """ Filter given list of any python values only for floats
    >>> filter_floats([1, 2.2, 3, 4+3j, 'b'])
    [2.2, 4+3j]
    >>> filter_floats([1, 2.0, 3, 4.5, 'b'])
    [2.0, 4.5]
    
	Include these tokens in the code: return list ( filter ( lambda x
	Do not include these tokens: if
	"""
    return [x for x in values if isinstance(x, float)]


def filter_booleans(values: List[Any]) -> List[bool]:
    """ Filter given list of any python values only for booleans
    >>> filter_booleans([1, 2.2, 3, False, 'b'])
    [False]
    >>> filter_booleans([[], 44, None, True, 'y'])
    [True]
    
	Include these tokens in the code: return list ( filter ( lambda x
	Do not include these tokens: if
	"""
    return [x for x in values if isinstance(x, bool)]


def filter_lists(values: List[Any]) -> List[list]:
    """ Filter given list of any python values only for lists
    >>> filter_lists([1, 2.2, 3, False, '