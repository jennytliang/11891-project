from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    
	Include these tokens in the code: mean
	Do not include these tokens in the code: center
	"""
    return sum([abs(number - sum(numbers) / len(numbers)) for number in numbers]) / len(numbers)


def median(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate the median of this dataset.
    The median is the middle number in a sorted list of numbers. There are an even
    number of numbers, so the median is the average of the two numbers located in
    the middle.
    >>> median([1.0, 2.0, 3.0, 4.0])
    2.5
    
	Include these tokens in the code: median, sorted
	Do not include these tokens in the code: center
	"""
    return sorted(numbers)[len(numbers) // 2]


def median_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Median Absolute Deviation
    around the median of this dataset.
    Median Absolute Deviation is the average absolute difference between each
    element and a centerpoint (median in this case):
    MAD = average | x - x_median |
    >>> median_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    
	Include these tokens in the code: median, sorted
	Do not include these tokens in the code: center
	"""
    return sum([abs(number - median(numbers)) for number in numbers]) / len(numbers)


def mode(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate the mode of this dataset.
    The mode is the most common value in a list.
    >>> mode([1.0, 2.0, 3.0, 4.0, 2.0, 2.0])
    2.0
    
	Include these tokens in the code: mode
	Do not include these tokens in the code: median, sorted
	"""
    return max(set(numbers), key=numbers.count)


def interquartile_range(numbers: List[float])