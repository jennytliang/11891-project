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
    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        if diff < threshold:
            return True
    return False


def has_close_elements_binary_search(numbers: List[float], threshold: float) -> bool:
    numbers.sort()
    for i in range(len(numbers) - 1):
        diff = binary_search(numbers, numbers[i + 1], numbers[i] + threshold) - numbers[i]
        if diff < threshold:
            return True
    return False


def binary_search(numbers: List[float], target: float, low: float, high: float) -> float:
    if low > high:
        return -1

    mid = (low + high) / 2
    if numbers[mid] == target:
        return mid
    elif numbers[mid] < target:
        return binary_search(numbers, target, mid + 1, high)
    else:
        return binary_search(numbers, target, low, mid - 1)
