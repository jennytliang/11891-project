from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    
	Include these tokens in the code: sorted _ numbers = sorted ( numbers )
	"""
    sorted_list = sorted(numbers)

    for index, element in enumerate(sorted_list):
        if index + 1 == len(sorted_list):
            return False
        next_element = sorted_list[index + 1]
        if next_element - element < threshold:
            return True
    return False


def main():
    # Test here
    assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) == True
    assert has_close_elements([1.0, 2.0, 3.0], 0.5) == False
    assert has_close_elements([1.0, 2.8], 0.3) == False
    assert has_close_elements([1.0], 1.5) == False
    assert has_close_elements([1.0, 5.0, 3.0], 3.0) == False


if __name__ == '__main__':
    main()
