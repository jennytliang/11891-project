from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    
	Do not include these tokens in the code: # calculate the mean
	"""
    mean = sum(numbers) / len(numbers)
    return sum([abs(x - mean) for x in numbers]) / len(numbers)


def median(numbers: List[float]) -> float:
    """ For a given list of input numbers, return the median value.
    Median is the middle number in a sorted list of numbers. There are an even
    number of numbers, so the median is the average of the two numbers in the
    middle.
    >>> median([1, 3, 5])
    3.0
    >>> median([1, 3, 5, 7])
    4.0
    """
    numbers.sort()
    return (numbers[len(numbers) // 2] + numbers[len(numbers) // 2 - 1]) / 2


def median2(numbers: List[float]) -> float:
    """ For a given list of input numbers, return the median value.
    Median is the middle number in a sorted list of numbers. There are an even
    number of numbers, so the median is the average of the two numbers in the
    middle.
    >>> median2([1, 3, 5])
    3.0
    >>> median2([1, 3, 5, 7])
    4.0
    """
    numbers.sort()
    if len(numbers) % 2 == 0:
        return (numbers[len(numbers) // 2] + numbers[len(numbers) // 2 - 1]) / 2
    else:
        return numbers[len(numbers) // 2]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
