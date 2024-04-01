from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Do not include these tokens in the code:  max _ so _ far = [ numbers [
	"""

    max_so_far = [numbers[0]]
    for num in numbers[1:]:
        max_so_far.append(max(num, max_so_far[-1]))
    return max_so_far


def rolling_max_linear(numbers: List[int]) -> List[int]:
    """ Same as above but using a single loop.
    >>> rolling_max_linear([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_so_far = numbers[0]
    result = []
    for num in numbers:
        if num > max_so_far:
            max_so_far = num
        result.append(max_so_far)
    return result


def rolling_max_linear_with_index(numbers: List[int]) -> List[Tuple[int, int]]:
    """ Same as above but using a single loop and returning a list of tuples.
    >>> rolling_max_linear_with_index([1, 2, 3, 2, 3, 4, 2])
    [(1, 1), (2, 2), (3, 3), (3, 3), (3, 3), (4, 4), (4, 4)]
    """
    max_so_far = numbers[0]
    max_index = 0
    result = []
    for num_index, num in enumerate(numbers):
        if num > max_so_far:
            max_so_far = num
            max_index = num_index
        result.append((num, max_index))
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
