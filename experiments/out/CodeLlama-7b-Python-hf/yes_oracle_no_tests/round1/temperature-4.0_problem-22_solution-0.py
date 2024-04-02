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


    return [v for v in values if isinstance(v, int)]


def filter_str_len(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings of a given length
    >>> filter_str_len(['a', 3.14, 5])
    []
    >>> filter_str_len(['a', 'bc', 'de'])
    ['a', 'bc']
	
	Include these tokens in the code: filter len
	Do not include these tokens in the code: Filter In te gers Context
	"""


    return [v for v in values if isinstance(v, str) and len(v) in [1, 2]]


def filter_even_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for even integers
    >>> filter_even_integers(['a', 3.14, 5])
    []
    >>> filter_even_integers([1, 2, 3, 'abc', {}, []])
    [2]
	
	Include these tokens in the code: filter even
	Do not include these tokens in the code: Filter Inte gers Context
	"""


    return [v for v in values if isinstance(v, int) and v % 2 == 0]


def filter_dicts(values: List[Any]) -> List[dict]:
    """ Filter given list of any python values only for dictionaries
    >>> filter_dicts(['a', 3.14, 5])
    []
    >>> filter_dicts([{}, [], 'abc', 1, 2])
    [{}, []]
	
	Include these tokens in the code: filter dict
	Do not include these tokens in the code: Filter Inte gers Context
	"""


    return [v for v in values if isinstance(v, dict)]


def filter_lists(values: List[Any]) -> List[list]:
    """ Filter given list of any python values only for lists
    >>> filter_lists(['a', 3.14, 5