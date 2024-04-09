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
	Do not include these tokens in the code: n
	"""

    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)


def median_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Median Absolute Deviation
    around the median of this dataset.
    Median Absolute Deviation is the average absolute difference between each
    element and a medianpoint:
    MAD = average | x - x_median |
    >>> median_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    
	Include these tokens in the code: x
	Do not include these tokens in the code: n
	"""
    median = sorted(numbers)[len(numbers) // 2]
    return sum(abs(x - median) for x in numbers) / len(numbers)


def median_absolute_deviation_percentage(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Median Absolute Deviation
    percentage around the median of this dataset.
    Median Absolute Deviation percentage is the average absolute difference
    between each element and a medianpoint expressed as a percentage of the
    median.
    MAD = average | x - x_median | / x_median * 100
    >>> median_absolute_deviation_percentage([1.0, 2.0, 3.0, 4.0])
    20.0
    
	Include these tokens in the code: x
	Do not include these tokens in the code: n
	"""
    median = sorted(numbers)[len(numbers) // 2]
    return sum(abs(x - median) / median * 100 for x in numbers) / len(numbers)
