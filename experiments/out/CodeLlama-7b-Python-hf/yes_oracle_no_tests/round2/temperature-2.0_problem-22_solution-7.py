from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    r: List[int] = []
    for v in values:
        if isinstance(v, int):
            r.append(v)
    return r


def filter_strings(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    
    >>> filter_strings(['a', 3.14, 5])
    ['a']
    >>> filter_strings([1, 2, 3, 'abc', {}, []])
    ['abc']

	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    r: List[str] = []
    for v in values:
        if isinstance(v, str):
            r.append(v)
    return r


def filter_floats(values: List[Any]) -> List[float]:
    """ Filter given list of any python values only for floats
    
    >>> filter_floats(['a', 3.14, 5])
    [3.14]
    >>> filter_floats([1, 2, 3, 'abc', {}, []])
    []
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    r: List[float] = []
    for v in values:
        if isinstance(v, float):
            r.append(v)
    return r


def filter_dicts(values: List[Any]) -> List[dict]:
    """ Filter given list of any python values only for dictionaries
    
    >>> filter_dicts(['a', 3.14, 5])
    []
    >>> filter_dicts([1, 2, 3, 'abc', {}, []])
    [{}, {}]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    r: List[dict] = []
    for v in values:
        if isinstance(v, dict):
            r.append(v)
    return