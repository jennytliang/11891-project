from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""


    res = []
    for i in range(len(numbers)):
        res.append(numbers[i])
        if i != len(numbers) - 1:
            res.append(delimeter)
    return res


def count_positives(numbers: List[int]) -> int:
    """ Count the number of positive numbers in the input list `numbers'
    >>> count_positives([1, 2, 3, -4, 0, 6])
    3
    >>> count_positives([1, -2, -3, -4, -5, -6])
    1
    >>> count_positives([0, 0, 0, 0, 0, 0])
    0
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""


def get_min_max(numbers: List[int]) -> (int, int):
    """ Return a tuple containing the minimum and maximum numbers of the input list `numbers'
    >>> get_min_max([1, 2, 3, -4, 0, 6])
    (-4, 6)
    >>> get_min_max([1, -2, -3, -4, -5, -6])
    (-6, -2)
    >>> get_min_max([0, 0, 0, 0, 0, 0])
    (0, 0)
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""


def get_min_max_naive(numbers: List[int]) -> (int, int):
    """ Return a tuple containing the minimum and maximum numbers of the input list `numbers'
    >>> get_min_max_naive([1, 2, 3, -4, 0, 6])
    (-4, 6)
    >>> get_min_max_naive([1, -2, -3, -4, -5, -6])
    (-6, -2)
    >>> get_min_max_naive([0, 0, 0, 0, 0, 0])
    (0, 0)
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""
