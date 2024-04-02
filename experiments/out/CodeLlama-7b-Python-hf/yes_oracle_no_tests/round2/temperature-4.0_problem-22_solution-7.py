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


def filter_strings(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings(['a', 3.14, 5])
    ['a']
    >>> filter_strings([1, 2, 3, 'abc', {}, []])
    ['abc']
    
	Include these tokens in the code: return list ( filter ( lambda x : type (
	"""
    return [x for x in values if isinstance(x, str)]


def filter_dicts(values: List[Any]) -> List[dict]:
    """ Filter given list of any python values only for dictionaries
    >>> filter_dicts(['a', 3.14, 5])
    []
    >>> filter_dicts([1, 2, 3, 'abc', {}, []])
    [{}, {}]
    
	Include these tokens in the code: return list ( filter ( lambda x : type (
	"""
    return [x for x in values if isinstance(x, dict)]


def filter_lists_tuples(values: List[Any]) -> List[list]:
    """ Filter given list of any python values only for lists and tuples
    >>> filter_lists_tuples(['a', 3.14, 5])
    []
    >>> filter_lists_tuples([1, 2, 3, 'abc', {}, []])
    [[], [1, 2, 3]]
    
	Include these tokens in the code: return list ( filter ( lambda x : type (
	"""
    return [x for x in values if isinstance(x, list) or isinstance(x, tuple)]


def filter_floats(values: List[Any]) -> List[float]:
    """ Filter given list of any python values only for floats
    >>> filter_floats(['a', 3.14, 5])
    [3.14]
    >>> filter_floats([1, 2, 3, 'abc', {}, []])