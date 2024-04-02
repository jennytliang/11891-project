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
    >>> filter_strings([1, 2.2, 'hello', 3, 'bye'])
    ['hello', 'bye']
    >>> filter_strings([[], 44, 'world'])
    ['world']
    
	Include these tokens in the code: return list ( filter ( lambda x : type (
	"""
    return [x for x in values if isinstance(x, str)]


def filter_lists(values: List[Any]) -> List[list]:
    """ Filter given list of any python values only for lists
    >>> filter_lists([1, 2, 3, 'str', {}, []])
    [[], []]
    >>> filter_lists([1, 2.2, 'str', 3, 'bye'])
    []
    
	Include these tokens in the code: return list ( filter ( lambda x : type (
	"""
    return [x for x in values if isinstance(x, list)]


def filter_tuples(values: List[Any]) -> List[tuple]:
    """ Filter given list of any python values only for tuples
    >>> filter_tuples([1, 2, 3, 'tuple', {}, []])
    []
    >>> filter_tuples([(1, 2), (3, 4), (5, 6)])
    [(1, 2), (3, 4), (5, 6)]
    
	Include these tokens in the code: return list ( filter ( lambda x : type (
	"""
    return [x for x in values if isinstance(x, tuple)]


def filter_dictionaries(values: List[Any]) -> List[dict]:
    """ Filter given list of any python values only for dictionaries
    >>> filter_dictionaries([1, 2, 3, 'dict', {}, []])
    [{}, {}]
    >>> filter_dictionaries([{'a': 1}, {'b': 2}])