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

def median(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate median

    >>> median([1.0, 2.0, 3.0, 4.0])
    2.5

	Include these tokens in the code: numbers sorted_numbers_copy
	Do not include these tokens in the code: num median sum sorted
	"""
    # your code here
    num1 = [sorted(numbers)]
    num2 = len(num1)/2
    num3 = sorted(numbers)
    num3 = int(num2)
    return num3


def skewness(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate skewness of this dataset.

    >>> skewness([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], 3.6)
    0.0

	Include these tokens in the code: numbers skewness_value
	Do not include these tokens in the code: num skew
	"""

    skewness_value = 0.0
    # Calculate mean and median first
    num1 = [numbers]
    num2 = medina(numbers)
    # Calculate M3 if possible
    num3 = [sum(pow(x - num2, 3) for x in num1)]
    num3 = num3[0]
    # Calculate skewness value
    num4 = pow(num3/len(num1), 1 / len(num1))
    return num4
    


if __name__ == "__main__":
	import doctest  # See https://docs.python.org/3/library/doctest.html
	doctest.testmod(verbose=True)  # verbose so we can see methods missing tests


