from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    
	Include these tokens in the code: diff
	Do not include these tokens in the code: d ifference
	"""



    numbers.sort()
 
    smallest_diff = numbers[0] - numbers[1]
    result_1 = numbers[0]
    result_2 = numbers[1]
 
    for i in range(len(numbers) - 1):
        diff = numbers[i] - numbers[i + 1]
        if diff < smallest_diff:
            smallest_diff = diff
            result_1 = numbers[i]
            result_2 = numbers[i + 1]
 
    return result_1, result_2


if __name__ == "__main__":
    import doctest
    doctest.testmod()
