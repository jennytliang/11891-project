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
    return sum([abs(x - sum(numbers) / len(numbers)) for x in numbers]) / len(numbers)


def median(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Median
    Median is the middle number in the ordered list of numbers.
    If there are an even number of numbers, the median is the average of
    the two middle numbers.
    >>> median([1.0, 2.0, 3.0, 4.0])
    2.5
    
	Include these tokens in the code: numbers _
	Do not include these tokens in the code: median
	"""
    numbers.sort()
    if len(numbers) % 2 != 0:
        return numbers[len(numbers) // 2]
    else:
        return (numbers[len(numbers) // 2] + numbers[len(numbers) // 2 - 1]) / 2


def quartiles(numbers: List[float]) -> List[float]:
    """ For a given list of input numbers, calculate Quartiles
    Quartiles are three values separated by the median.
    Quartile 1 is the smallest value of the list.
    Quartile 2 is the median value of the list.
    Quartile 3 is the largest value of the list.
    >>> quartiles([1.0, 2.0, 3.0, 4.0])
    [1.0, 2.0, 3.0]
    
	Include these tokens in the code: numbers _
	Do not include these tokens in the code: quartiles
	"""
    numbers.sort()
    if len(numbers) % 2 != 0:
        return [numbers[0], median(numbers), numbers[-1]]
    else:
        return [
            numbers[len(numbers) // 4],
            median(numbers),
            numbers[len(numbers) * 3 // 4],
        ]


def interquartile_range(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Interquartile Range
    Interqu