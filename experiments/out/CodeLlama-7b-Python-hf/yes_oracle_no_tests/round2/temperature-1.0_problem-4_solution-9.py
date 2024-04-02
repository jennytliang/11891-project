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
    import doctest

    doctest.testmod(verbose=True)

    user_input = input(
        "Enter the list of numbers to calculate Mean Absolute Deviation: "
    ).strip()
    input_list = [float(x) for x in user_input.split()]
    print(f"The Mean Absolute Deviation is {mean_absolute_deviation(input_list)}")