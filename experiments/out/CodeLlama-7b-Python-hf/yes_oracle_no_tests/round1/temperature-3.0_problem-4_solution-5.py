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
    # calculate mean
    mean = sum(numbers) / len(numbers)
    # calculate absolute deviations from the mean
    deviations = []
    for number in numbers:
        deviation = abs(number - mean)
        deviations.append(deviation)
    # calculate the mean of the absolute deviations
    return sum(deviations) / len(deviations)


if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))
