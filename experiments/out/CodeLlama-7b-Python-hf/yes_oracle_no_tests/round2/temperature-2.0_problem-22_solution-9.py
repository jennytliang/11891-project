from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    
	Include these tokens in the code: lambda x
	Do not include these tokens in the code: l amba value
	"""


    return list(f for f in values if isinstance(f, int))


def filter_strings(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings(['a', 3.14, 5])
    ['a']
    >>> filter_strings([1, 2, 3, 'abc', {}, []])
    ['abc']
    
	Include these tokens in the code: lambda x
	Do not include these tokens in the code: l amba value
	"""


    return list(f for f in values if isinstance(f, str))


def filter_dicts(values: List[Any]) -> List[dict]:
    """ Filter given list of any python values only for dicts
    >>> filter_dicts([{'a': 1}, {'b': 2, 'c': 3}])
    [{'a': 1}, {'b': 2, 'c': 3}]
    >>> filter_dicts([1, 2, 3, 'abc', {}, []])
    []
    
	Include these tokens in the code: lambda x
	Do not include these tokens in the code: l amba value
	"""


    return list(f for f in values if isinstance(f, dict))