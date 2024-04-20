from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    
	Include these tokens in the code: sum
	Do not include these tokens in the code: su
	"""



    mean = sum(numbers) / len(numbers)
    return sum([abs(num - mean) for num in numbers]) / len(numbers)


print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))
print(mean_absolute_deviation([3.0, 1.0]))
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 100.0]))