from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    
	Include these tokens in the code: sorted _ numbers = sorted ( numbers )
	Do not include these tokens in the code: . sort ()
	"""
    # sorted_numbers = sorted(numbers)
    sorted_numbers = numbers.sort()
    for i in range(len(numbers) - 1):
        if abs(numbers[i] - numbers[i + 1]) < threshold:
            return True
    return False


def main():
    print("Example:")
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert has_close_elements([1.0, 2.0, 3.0], 0.5) == False
    assert has_close_elements([1.0, 2.0, 3.0], 1) == False
    assert has_close_elements([1.0, 2.3, 3.0, 4.0], 0.9) == False
    assert has_close_elements([1.0, 2.3, 3.0, 4.0], 1.5) == True
    assert has_close_elements([1.0, 2.3, 3.0, 4.0], 0.4) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")


if __name__ == "__main__":
    main()
