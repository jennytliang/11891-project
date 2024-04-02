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

    return list(filter(lambd: isinstance(lambd, int), values))


def filter_strings(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings(['a', 3.14, 5])
    ['a']
    >>> filter_strings([1, 2, 3, 'abc', {}, []])
    ['abc']
    
	Include these tokens in the code: type
	Do not include these tokens in the code: is instance
	"""
    return list(filter(lambda lambd: isinstance(lambd, str), values))


def filter_dicts(values: List[Any]) -> List[dict]:
    """ Filter given list of any python values only for dictionaries
    >>> filter_dicts(['a', 3.14, 5])
    []
    >>> filter_dicts([1, 2, 3, 'abc', {}, []])
    [{}]
    
	Include these tokens in the code: type
	Do not include these tokens in the code: is instance
	"""
    return list(filter(lambda lambd: isinstance(lambd, dict), values))


def filter_lists(values: List[Any]) -> List[list]:
    """ Filter given list of any python values only for lists
    >>> filter_lists(['a', 3.14, 5])
    []
    >>> filter_lists([1, 2, 3, 'abc', {}, []])
    [[], [1, 2, 3]]
    
	Include these tokens in the code: type
	Do not include these tokens in the code: is instance
	"""
    return list(filter(lambda lambd: isinstance(lambd, list), values))


def filter_tuples(values: List[Any]) -> List[tuple]:
    """ Filter given list of any python values only for tuples
    >>> filter_tuples(['a', 3.14, 5])
    []
    >>> filter_tuples([1, 2, 3, 'abc', {}, []])
    [