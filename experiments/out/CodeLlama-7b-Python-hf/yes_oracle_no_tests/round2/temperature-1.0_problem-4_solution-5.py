from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    
	Include these tokens in the code: return sum (
	Do not include these tokens in the code: abs _ mean _ diff = [
	"""

   
    mean = sum(numbers) / len(num_list)

	# Write your code above 👆

    return abs(sum(numbers) / len(num_list) - mean_absolute_deviation) / len(num_list)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(
        mean_absolute_deviation(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 1.4, 3), "Mean absolute deviation (1)"

    assert almost_equal(mean_absolute_deviation(
        [-10, 1, 2, 3, 4, 5, 6, 7, 8, 9]), 3.25, 3), "Mean absolute deviation (2)"

    assert almost_equal(
        mean_absolute_deviation(
            [1.23, 0.2, -10, -0.5, 13]), 1.275, 3), "Mean absolute deviation (3)"

    assert almost_equal(mean_absolute_deviation([-1, -2]), 1.5, 3), "Mean absolute deviation (4)"

    assert almost_equal(
        mean_absolute_deviation([1, 2, 4, -3]), 0.75, 3), "Mean absolute deviation (5)"
