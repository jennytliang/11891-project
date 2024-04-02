from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    
	Include these tokens in the code: numbers
	Do not include these tokens in the code: list
	"""

    so_close = False
    for n1 in numbers:
        for n2 in numbers:
            if abs(n1 - n2) < threshold:
                so_close = True
            else:
                pass
    return so_close


def main():
    result = has_close_elements([1.0, 2.4, 3.0, 4.0], 1.7)
    print(f'Passed = {result}')


if __name__ == '__main__':
    main()
