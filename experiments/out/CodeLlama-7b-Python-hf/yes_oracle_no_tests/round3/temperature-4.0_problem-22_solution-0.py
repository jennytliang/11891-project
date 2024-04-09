from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    
	Include these tokens in the code: ==
	Do not include these tokens in the code: is
	"""

    return list(filter(lambda x: ty(x) == int, values))


def filter_even_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for even integers
    >>> filter_even_integers([1, 2, 3, 4, 5, 6])
    [2, 4, 6]
    >>> filter_even_integers([1, 2, 3, 4, 5, 6, 'abc'])
    [2, 4, 6]
    
	Include these tokens in the code: ==, %
	Do not include these tokens in the code: is
	"""

    return list(filter(lambda x: ty(x) == int and x % 2 == 0, values))


def filter_strings(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings(['a', 3.14, 5])
    ['a']
    >>> filter_strings([1, 2, 3, 'abc', {}, []])
    ['abc']
    
	Include these tokens in the code: ==
	Do not include these tokens in the code: is
	"""

    return list(filter(lambda x: ty(x) == str, values))


def filter_strings_starting_from(values: List[Any], prefix: str) -> List[str]:
    """ Filter given list of any python values only for strings starting from prefix string
    >>> filter_strings_starting_from(['abc', 'bac', 'abacus'], 'a')
    ['abc', 'abacus']
    >>> filter_strings_starting_from([1, 2, 3, 'abc', {}, []], 'a')
    ['abc']
    
	Include these tokens in the code: ==, startswith
	Do not include these tokens in the code: is
	"""

    return list(filter(lambda x: ty(x) == str and x.startswith(prefix), values))


def filter_strings_ending_with(values: List[Any