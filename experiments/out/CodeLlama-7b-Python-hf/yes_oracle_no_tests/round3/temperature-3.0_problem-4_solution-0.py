from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    
	Include these tokens in the code: numbers
	Do not include these tokens in the code: num be
	"""


    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers)  / len(numbers)



def main():
    numbers = [1.0, 2.0, 3.0, 4.0]
    assert mean_absolute_deviation(numbers) == 1.0
    numbers = [1.0, 2.0, 3.0, 4.0, 1.0, 5.0, 2.0, 6.0]
    assert mean_absolute_deviation(numbers) == 1.5
    numbers = [2.0, 1.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]
    assert mean_absolute_deviation(numbers) == 1.0
    numbers = [2.0, 1.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 2.0, 1.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]
    assert mean_absolute_deviation(numbers) == 1.0
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    assert mean_absolute_deviation(numbers) == 1.4
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    assert mean_absolute_deviation(numbers) == 1.2
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
    assert mean_absolute_deviation(numbers) == 1.2
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]
    assert mean_absolute_deviation(numbers) == 1.2
    numbers = [1.0, 