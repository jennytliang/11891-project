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

    numbers.sort(reverse=False)
    min_diff = float('inf')
    result1 = numbers[0]
    result2 = numbers[0]
    for number1 in numbers:
        for number2 in numbers:
            if number1 < number2:
                diff = number2 - number1
                if diff < min_diff:
                    min_diff = diff
                    result1 = number1
                    result2 = number2

    return result1, result2


def find_closest_elements2(numbers: List[float]) -> Tuple[float, float]:
    """ Same approach as in previous exercise with a bit more concise code.
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    
	Include these tokens in the code: min_diff =
	Do not include these tokens in the code: __
	"""

    numbers.sort(reverse=False)
    min_diff = float('inf')
    result1 = numbers[0]
    result2 = numbers[0]
    for i, number1 in enumerate(numbers):
        for number2 in numbers[i + 1:]:
            if number1 < number2:
                diff = number2 - number1
                if diff < min_diff:
                    min_diff = diff
                    result1 = number1
                    result2 = number2

    return result1, result2


if __name__ == '__main__':
    import doctest

    doctest.testmod()
