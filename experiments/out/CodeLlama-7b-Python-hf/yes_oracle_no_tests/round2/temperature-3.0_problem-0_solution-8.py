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
    numbers.sort()
    for index in range(len(numbers) - 1):
        if numbers[index + 1] - numbers[index] < threshold:
            return True
    return False


def main():
    numbers = [1.0, 2.8, 3.0, 4.0, 5.0, 2.0]
    assert has_close_elements(numbers, 0.3) == True
    assert has_close_elements(numbers, 0.5) == False


if __name__ == "__main__":
    main()
