from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    
	Include these tokens in the code: ) / len
	Do not include these tokens in the code: )/
	"""

    mean = sum(nu for nu in numbers) / len(numbers)
    return sum(abs(nu - mean) for nu in numbers) / len(numbers)


def main():
    numbers = [1.0, 2.0, 3.0, 4.0]
    result = mean_absolute_deviation(numbers)
    print(result)


if __name__ == "__main__":
    main()
