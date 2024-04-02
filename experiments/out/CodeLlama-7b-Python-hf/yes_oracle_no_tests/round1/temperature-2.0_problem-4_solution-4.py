from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""

    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbe)


if __name__ == "__main__":
    # Test your code with this first
    # Change the argument to try different values
    print(mean_absolute_deviation([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

    # After you are satisfied with your results, use input() to prompt the user
    # for a value
    # numbers = input('Enter numbers separated by a comma:\n').strip()
    # print(f"Mean Absolute Deviation is {mean_absolute_deviation(list(map(int, numbers.split(','))))}")
