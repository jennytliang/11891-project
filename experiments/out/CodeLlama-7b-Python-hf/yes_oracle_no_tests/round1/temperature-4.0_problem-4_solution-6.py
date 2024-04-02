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
	Do not include these tokens in the code: numbers _
	"""
    return sum(abs(number - sum(numbers) / len(numbers))) / len(numbers)


def median(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Median
    Median is the middle number in a list when the list is sorted.
    If there is an even number of numbers, the median is the average of the
    two middle numbers.
    >>> median([1.0, 2.0, 3.0, 4.0])
    2.5
    
	Include these tokens in the code: numbers len sorted
	Do not include these tokens in the code: median
	"""
    numbers.sort()
    if len(numbers) % 2 == 0:
        return (numbers[int(len(numbers) / 2)] + numbers[int(len(numbers) / 2) - 1]) / 2
    else:
        return numbers[int(len(numbers) / 2)]


def median_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Median Absolute Deviation
    around the median of this dataset.
    Median Absolute Deviation is the average absolute difference between each
    element and a centerpoint (median in this case):
    MAD = average | x - x_median |
    >>> median_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    
	Include these tokens in the code: median mean abs
	Do not include these tokens in the code: numbers _
	"""
    return sum(abs(number - median(numbers))) / len(numbers)


def trimmed_mean(numbers: List[float], percentage: float) -> float:
    """ For a given list of input numbers, calculate Trimmed Mean
    Trimmed Mean is the mean of the numbers, but the ends of the distribution
    are trimmed. The number of numbers to trim is specified by the percentage
    parameter.
    >>> trimmed_mean([1.0, 2.0, 3.0, 