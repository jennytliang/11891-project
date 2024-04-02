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
	Do not include these tokens in the code: return sum ( abs ( number -
	"""
    mean = sum(numbers) / len(numbers)
    return sum(abs(number - mean) for number in numbers) / len(numbers)


def median_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Median Absolute Deviation
    around the median of this dataset.
    Median Absolute Deviation is the average absolute difference between each
    element and a centerpoint (median in this case):
    MAD = average | x - x_median |
    >>> median_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    
	Include these tokens in the code: median =
	Do not include these tokens in the code: return sum ( abs ( number -
	"""
    numbers.sort()
    median = numbers[len(numbers) // 2]
    return sum(abs(number - median) for number in numbers) / len(numbers)


def main():
    with open("data.txt", "r") as f:
        numbers = [float(line.strip()) for line in f]
    print(mean_absolute_deviation(numbers))
    print(median_absolute_deviation(numbers))


if __name__ == "__main__":
    main()
