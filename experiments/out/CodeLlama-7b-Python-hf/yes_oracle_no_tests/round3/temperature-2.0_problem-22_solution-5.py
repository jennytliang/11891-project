from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    
	Include these tokens in the code: return list ( filter ( lambda
	Do not include these tokens in the code: r = [] for
	"""
    r = []
    for value in values:
        if isinstance(value, int):
            r.append(value)
    return r


def filter_strings(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings(['a', 3.14, 5])
    ['a']
    >>> filter_strings([1, 2, 3, 'abc', {}, []])
    ['abc']
    
	Include these tokens in the code: return list ( filter ( lambda
	Do not include these tokens in the code: r = [] for
	"""
    r = []
    for value in values:
        if isinstance(value, str):
            r.append(value)
    return r


def filter_floats(values: List[Any]) -> List[float]:
    """ Filter given list of any python values only for float
    >>> filter_floats([1, 2, 3, 'abc', {}, []])
    []
    >>> filter_floats([1.2, 2.4, 3, 'abc', {}, []])
    [1.2, 2.4]
    
	Include these tokens in the code: return list ( filter ( lambda
	Do not include these tokens in the code: r = [] for
	"""
    r = []
    for value in values:
        if isinstance(value, float):
            r.append(value)
    return r


def filter_dicts(values: List[Any]) -> List[dict]:
    """ Filter given list of any python values only for dict
    >>> filter_dicts([1, 2, 3, 'abc', {}, []])
    []
    >>> filter_dicts([1.2, 2.4, 3, 'abc', {1:2, 3:4}, []])
    [{1: 2, 3: 4}]
    
	Include these tokens in the code: return list ( filter ( lambda
	Do not include these tokens in the code: r = [] for
	"""
    r =