from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    
	Include these tokens in the code: list ( filter ( lambda
	Do not include these tokens in the code: [ x for
	"""

    r = []
    for v in values:
        if isinstance(v, int):
            r.append(v)
    return r


def filter_strings(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    
	>>> filter_strings(['a', 3.14, 'xyz'])
	['a', 'xyz']
	>>> filter_strings([1, 2, 3, 'abc', {}, []])
	['abc']
    
	Include these tokens in the code: list ( filter ( lambda
	Do not include these tokens: [ x for
	"""

    r = []
    for v in values:
        if isinstance(v, str):
            r.append(v)
    return r


def filter_dicts(values: List[Any]) -> List[dict]:
    """ Filter given list of any python values only for dictionaries
    
	>>> filter_dicts([{'a': 1}, {'b': 2}, [1, 2, 3], 'xyz'])
	[{'a': 1}, {'b': 2}]
	>>> filter_dicts([1, 2, 3, {'a': 4}, 'xyz'])
	[{'a': 4}]
    
	Include these tokens in the code: list ( filter ( lambda
	Do not include these tokens: [ x for
	"""

    r = []
    for v in values:
        if isinstance(v, dict):
            r.append(v)
    return r


def filter_lists(values: List[Any]) -> List[list]:
    """ Filter given list of any python values only for lists
    
	>>> filter_lists([[1, 2, 3], {'a': 4}, 'xyz'])
	[[1, 2, 3]]
	>>> filter_lists([1, 2, 3, [4, 5, 6], 'xyz'])
	[[4, 5, 6]]
    
	Include these tokens in the code: list ( filter ( lambda
	Do not