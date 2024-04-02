from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    
	Include these tokens in the code: x
	Do not include these tokens in the code: number
	"""

    mean = sum(numbers) / len(numbers)
    return sum([abs(number - mean) for number in numbers]) / len(numbers)


def median(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate the median.
    The median is defined to be the middle number in a sorted
    list. If there are an even number of numbers, mean them.
    >>> median([1, 2, 3, 4])
    2.5
    
	Include these tokens in the code: return, numbers, sorted, number
	Do not include these tokens in the code: number, median
	"""
    numbers.sort()
    return sum(numbers) / len(numbers) if len(numbers) % 2 == 0 else numbers[int(len(numbers)/2)]

def mean(numbers: List[float]) -> float:
    """ Calculate the mean value of a list of numbers.

	>>> mean([1, 2, 3, 4])
    2.5
    
	Include these tokens in the code: sum, int
	Do not include these tokens in the code: 
		* mean, numbers, len
	"""
    return sum(numbers) / len(numbers)

def mode(numbers: List[int]) -> List[int]:
    """ Calculate the most frequent element in a list of numbers.
    (Assume the list is composed of integers.)
    If a number appears as often as any other number, then return
    a list with the mode, otherwise return an empty list.

	>>> mode([1, 2, 3, 4, 5, 6])
    []
	>>> mode([1, 2, 2, 3, 3, 3])
    [2, 3]
    
	Include these tokens in the code: numbers, int, list
	Do not include these tokens in the code: number, sum, min, max
	"""
    if len(numbers) < 1:
        return []
    c = 0
    res = []
    for i in numbers:
        c = numbers.count(i)
        if c == len(numbers):
            return [