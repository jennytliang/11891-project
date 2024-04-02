from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    
	Do not include these tokens in the code: # calculate mean
	"""
    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)


def main():
    print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))
    print(mean_absolute_deviation([0.0, 12.23, 0.0]))
    print(mean_absolute_deviation([0.0, 12.23, 5.0, 0.0]))
    print(mean_absolute_deviation([0.0, 12.23, 5.0, 18.0]))
    print(mean_absolute_deviation([0.0, 12.23, 5.0, 18.0, 20.0]))


if __name__ == "__main__":
    main()