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


    return [x for x in values if type(x) is int]


def filter_strings(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings([1, 2, 3, 'abc', {}, []])
    ['abc']
    
	Include these tokens in the code: filter
	Do not include these tokens in the code: Filter In te gers Context
	"""


    return [x for x in values if type(x) is str]


def filter_empty_values(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for empty values
    >>> filter_empty_values(['a', 3.14, 0, '', [], {}, 5])
    ['a', 3.14, 0, '', [], {}]
    
	Include these tokens in the code: filter
	Do not include these tokens in the code: Filter In te gers Context
	"""


    return [x for x in values if not x]


def filter_primes(values: List[int]) -> List[int]:
    """ Filter given list of integers only for prime numbers
    >>> filter_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    [2, 3, 5, 7, 11]
    
	Include these tokens in the code: filter
	Do not include these tokens in the code: Filter In te gers Context
	"""


    return [x for x in values if all(x % i for i in range(2, x))]


def filter_divisible_by_5(values: List[int]) -> List[int]:
    """ Filter given list of integers only for numbers divisible by 5
    >>> filter_divisible_by_5([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    [5, 10]
