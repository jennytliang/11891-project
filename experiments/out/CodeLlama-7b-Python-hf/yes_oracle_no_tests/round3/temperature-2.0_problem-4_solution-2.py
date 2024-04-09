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
	Do not include these tokens in the code: number
	"""



    mean = sum(numbers) / len(numbers)

    return sum(abs(number - mean) for number in numbers) / len(numbers)


def main():
    print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))
    print(mean_absolute_deviation([1.0, 1.125, 1.25, 1.375, 1.5, 1.625, 1.75, 1.875, 2.0]))
    print(mean_absolute_deviation([3.0, 3.125, 3.25, 3.375, 3.5, 3.625, 3.75, 3.875, 4.0]))


if __name__ == "__main__":
    main()