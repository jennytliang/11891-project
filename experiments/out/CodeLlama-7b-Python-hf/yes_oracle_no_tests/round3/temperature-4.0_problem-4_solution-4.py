from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    
	Do not include these tokens in the code: # ST ART S OL UT ION
	"""
    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)


if __name__ == "__main__":
    # This part is for manual testing and is not needed for Automatic Evaluation
    print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))
    print(mean_absolute_deviation([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
