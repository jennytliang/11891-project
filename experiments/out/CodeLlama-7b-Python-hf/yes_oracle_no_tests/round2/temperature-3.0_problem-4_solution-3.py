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
	Do not include these tokens in the code: return sum ( abs ( n -
	"""
    pass


def main():
    print("Example:")
    print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == 1.0
    assert mean_absolute_deviation([0, 0, 0, 0]) == 0
    assert mean_absolute_deviation([-15.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0,
                                    100.0]) == 21 / 9
    print("Coding complete? Click 'Check' to earn cool rewards!")


if __name__ == '__main__':
    main()
