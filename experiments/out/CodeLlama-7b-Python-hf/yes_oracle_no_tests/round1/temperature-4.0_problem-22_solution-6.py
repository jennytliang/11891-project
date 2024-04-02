from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    
	Include these tokens in the code: filter
	Do not include these tokens in the code: Filter In te gers Context
	"""


    return [x for x in values if isinstance(x, int)]


def filter_strings(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings([1, 2.2, 'a', 'bc'])
    ['a', 'bc']
    >>> filter_strings([1, 2, 3, 'abc', {}, []])
    ['abc']
    
	Include these tokens in the code: filter
	Do not include these tokens in the code: Filter In te gers Context
	"""


    return [x for x in values if isinstance(x, str)]


def filter_dicts(values: List[Any]) -> List[dict]:
    """ Filter given list of any python values only for dicts
    >>> filter_dicts([1, 2.2, {'a': 1}, [1, 2, 3]])
    [{'a': 1}]
    >>> filter_dicts([1, 2, 3, 'abc', {}, []])
    []
    
	Include these tokens in the code: filter
	Do not include these tokens in the code: Filter In te gers Context
	"""


    return [x for x in values if isinstance(x, dict)]


def filter_lists(values: List[Any]) -> List[list]:
    """ Filter given list of any python values only for lists
    >>> filter_lists([1, 2.2, [1,2,3], {'a': 1}])
    [[1, 2, 3]]
    >>> filter_lists([1, 2, 3, 'abc', {}, []])
    [[]]
    
	Include these tokens in the code: filter
	Do not include these tokens in the code: Filter In te gers Context
	"""


    return [x for x in values if isinstance(x, list)]


def filter_booleans(values: List[Any]) -> List[bool]:
    """ Filter given list of any python values only for booleans
    >>> filter_booleans([1, 2