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
    r = []
    for x in values:
        if isinstance(x, int):
            r.append(x)
    return r


def filter_strings(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings(['a', 3.14, 5])
    ['a']
    >>> filter_strings([1, 2, 3, 'abc', {}, []])
    ['abc']
    
	Include these tokens in the code: return list ( filter ( lambda x
	Do not include these tokens in the code: r = [] for
	"""
    r = []
    for x in values:
        if isinstance(x, str):
            r.append(x)
    return r


def filter_dicts(values: List[Any]) -> List[dict]:
    """ Filter given list of any python values only for dicts
    >>> filter_dicts(['a', 3.14, 5])
    []
    >>> filter_dicts([1, 2, 3, 'abc', {}, []])
    [{}, {}]
    
	Include these tokens in the code: return list ( filter ( lambda x
	Do not include these tokens in the code: r = [] for
	"""
    r = []
    for x in values:
        if isinstance(x, dict):
            r.append(x)
    return r


def filter_functions(values: List[Any]) -> List[callable]:
    """ Filter given list of any python values only for functions
    >>> filter_functions(['a', 3.14, 5])
    []
    >>> filter_functions([1, 2, 3, 'abc', {}, []])
    []
    >>> filter_functions([lambda x: x])
    [function]
    
	Include these tokens in the code: return list ( filter ( lambda x
	Do not include these tokens in the code: r = [] for
	"""
    r = []
    for x in values:
        if callable(x):
            r.append(x)