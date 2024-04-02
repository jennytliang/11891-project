from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    
	Include these tokens in the code: mean =
	Do not include these tokens in the code: return sum ([ abs ( x -
	"""
    # START SOLUTION
    mean = sum(numbers) / len(numbers)

    return sum([abs(x - mean) for x in numbers]) / len(numbers)
    # END SOLUTION


def median_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Median Absolute Deviation
    around the median of this dataset.
    Median Absolute Deviation is the average absolute difference between each
    element and a centerpoint (median in this case):
    MAD = average | x - x_median |
    >>> median_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    
	Include these tokens in the code: median =
	Do not include these tokens in the code: return sum ([ abs ( x -
	"""
    # START SOLUTION
    numbers = sorted(numbers)
    median = numbers[len(numbers) // 2]

    return sum([abs(x - median) for x in numbers]) / len(numbers)
    # END SOLUTION


def main():
    numbers = [1.0, 2.0, 3.0, 4.0]
    assert mean_absolute_deviation(numbers) == 1.0
    assert median_absolute_deviation(numbers) == 1.0


if __name__ == "__main__":
    main()
