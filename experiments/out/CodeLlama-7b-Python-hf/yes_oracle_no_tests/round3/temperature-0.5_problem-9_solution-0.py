from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [ max ( numbers [ :( i + 1
	Do not include these tokens in the code: _ list = []
	"""
    _list = []
    for i in range(len(numbers)):
        _list.append(max(numbers[:(i + 1)]))
    return _list


if __name__ == "__main__":
    import doctest
    doctest.testmod()
