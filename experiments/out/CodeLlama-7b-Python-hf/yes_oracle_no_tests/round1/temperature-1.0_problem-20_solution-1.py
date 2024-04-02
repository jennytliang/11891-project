from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    
	Include these tokens in the code: min _ diff = float (" inf ")
	Do not include these tokens in the code: return
	"""

    numbers.sort(reverse=True)

    min_diff = float("inf")	# Initial difference set to Infinity

    for index in range(1, len(numbers)-1):
        diff = abs(numbers[index-1] - numbers[index])
        if diff <= min_diff:		# Check if the difference is now smaller than the previous smallest difference
            min_diff = diff
            min_diff_min_number = numbers[index-1]		# Determining which numbers that are in the range are the smallest, we will need them later
            min_diff_max_number = numbers[index]

    return min_diff_min_number, min_diff_max_number



if __name__ == "__main__":
    import doctest
    # from testlib import test_file
    doctest.testmod()
    # test_file("closest_elem.py")