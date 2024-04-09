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

    r = list(filter(lambda x: isinstance(x, int), values))
    return r


def filter_strings(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings(['a', 3.14, 5])
    ['a']
    >>> filter_strings([1, 2, 3, 'abc', {}, []])
    ['abc']
    
	Include these tokens in the code: list ( filter ( lambda
	Do not include these tokens: [ x for
    """

    r = list(filter(lambda x: isinstance(x, str), values))
    return r


def filter_booleans(values: List[Any]) -> List[bool]:
    """ Filter given list of any python values only for booleans
    >>> filter_booleans(['a', 3.14, 5])
    []
    >>> filter_booleans([1, 2, 3, 'abc', {}, []])
    []
    
	Include these tokens in the code: list ( filter ( lambda
	Do not include these tokens: [ x for
    """

    r = list(filter(lambda x: isinstance(x, bool), values))
    return r


def filter_dicts(values: List[Any]) -> List[dict]:
    """ Filter given list of any python values only for dictionaries
    >>> filter_dicts(['a', 3.14, 5])
    []
    >>> filter_dicts([1, 2, 3, 'abc', {}, []])
    [{}]
    
	Include these tokens in the code: list ( filter ( lambda
	Do not include these tokens: [ x for
    """

    r = list(filter(lambda x: isinstance(x, dict), values))
    return r


def filter_lists(values: List[Any]) -> List[List]:
    """ Filter given list of any python values only for lists
    >>> filter_lists(['a', 3.14, 5])
    []
    >>> filter_lists([1, 2, 