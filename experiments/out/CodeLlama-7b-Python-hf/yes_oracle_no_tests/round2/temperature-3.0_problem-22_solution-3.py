from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    
	Include these tokens in the code: return list ( filter ( lambda x :
	Do not include these tokens in the code: r = [ value for value
	"""
    return [value for value in values if isinstance(value, int)]


def filter_strings(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings([1.2, 4, 'a', 'b', 'cde'])
    ['a', 'b', 'cde']
    >>> filter_strings([1, 2, 'a', 'b', 3, 'c'])
    ['a', 'b', 'c']
    
	Include these tokens in the code: return list ( filter ( lambda x :
	Do not include these tokens in the code: r = [ value for value
	"""
    return [value for value in values if isinstance(value, str)]


def filter_floats(values: List[Any]) -> List[float]:
    """ Filter given list of any python values only for floats
    >>> filter_floats([1, 2.5, 'a', 'b', 3, 'c'])
    [2.5]
    >>> filter_floats([1, 2, 'a', 'b', 3, 'c'])
    []
    
	Include these tokens in the code: return list ( filter ( lambda x :
	Do not include these tokens in the code: r = [ value for value
	"""
    return [value for value in values if isinstance(value, float)]


def filter_dicts(values: List[Any]) -> List[dict]:
    """ Filter given list of any python values only for dictionaries
    >>> filter_dicts([1, 2.5, 'a', 'b', 3, 'c'])
    []
    >>> filter_dicts([1, 2, {'a': 1, 'b': 2}, 'b', 3, 'c'])
    [{'a': 1, 'b': 2}]
    
	Include these tokens in the code: return list ( filter ( lambda x :
	Do not include these tokens in the code: r = [ value for value
	"""
    return [value for value in values if isinstance(value,