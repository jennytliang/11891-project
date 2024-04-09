from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: numbers [ :( i + 1
	Do not include these tokens in the code: nu
	"""


    return [max(numbers[:i + 1]) for i in range(len(numbers))]


def find_missing_num(numbers: List[int]) -> int:
    """ From a given list of numbers find a missing number.
    >>> find_missing_num([1, 2, 4, 5, 6, 7, 9, 10])
    3
    
	Include these tokens in the code: numbers [ :
	Do not include these tokens in the code: nu
	"""


    return sum([i * n for i, n in enumerate(numbers)]) - sum(numbers)


def find_first_repeated_num(numbers: List[int]) -> int:
    """ From a given list of numbers find a first repeated number.
    >>> find_first_repeated_num([1, 2, 3, 4, 5, 6, 6])
    6
    
	Include these tokens in the code: numbers [ :
	Do not include these tokens in the code: nu
	"""


    return next(n for i, n in enumerate(numbers) if numbers.count(n) > 1)


def find_first_repeated_num_2(numbers: List[int]) -> int:
    """ From a given list of numbers find a first repeated number.
    >>> find_first_repeated_num_2([1, 2, 3, 4, 5, 6, 6])
    6
    
	Include these tokens in the code: numbers [ :
	Do not include these tokens in the code: nu
	"""


    return next(n for n in numbers if numbers.count(n) > 1)


def find_first_repeated_num_3(numbers: List[int]) -> int:
    """ From a given list of numbers find a first repeated number.
    >>> find_first_repeated_num_3([1, 2, 3, 4, 5, 6, 6])
    6
    
	Include these tokens in the code: numbers [ :
	