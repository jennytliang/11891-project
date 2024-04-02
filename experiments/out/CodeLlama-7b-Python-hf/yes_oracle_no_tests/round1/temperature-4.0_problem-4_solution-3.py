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
    return sum(abs(mean(numbers) - num) for num in numbers) / len(numbers)


def median(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Median
    Args:
        numbers (List[float]): list of numbers
    Returns:
        float: median of the list of numbers
    """
    numbers.sort()
    return numbers[len(numbers) // 2]


def mean(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean
    Args:
        numbers (List[float]): list of numbers
    Returns:
        float: mean of the list of numbers
    """
    return sum(numbers) / len(numbers)


def median_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Median Absolute Deviation
    Args:
        numbers (List[float]): list of numbers
    Returns:
        float: median absolute deviation of the list of numbers
    """
    return median([abs(num - median(numbers)) for num in numbers])


def trimmed_mean(numbers: List[float], proportion_to_trim: float) -> float:
    """ For a given list of input numbers, calculate Trimmed Mean
    Args:
        numbers (List[float]): list of numbers
        proportion_to_trim (float): proportion of the numbers to trim
    Returns:
        float: trimmed mean of the list of numbers
    """
    numbers.sort()
    start = int(proportion_to_trim / 2 * len(numbers))
    end = len(numbers) - int(proportion_to_trim / 2 * len(numbers))
    return mean(numbers[start:end])


def trimmed_median(numbers: List[float], proportion_to_trim: float) -> float:
    """ For a given list of input numbers, calculate Trimmed Median
    Args:
        numbers (List[float]): list of numbers
        proportion_to_trim (float):