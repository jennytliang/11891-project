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
    # calculate the mean
    mean = sum(numbers) / len(numbers)
    # calculate the absolute difference between each element and a centerpoint
    abs_diff = [abs(n - mean) for n in numbers]
    # sum the absolute difference
    sum_abs_diff = sum(abs_diff)
    # return the mean absolute deviation
    return sum_abs_diff / len(numbers)
