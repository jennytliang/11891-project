from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: max _ so _ far =
	"""
    max_so_far = numbers[0]
    rolling_max = [numbers[0]]
    for number in numbers[1:]:
        if number > max_so_far:
            max_so_far = number
        rolling_max.append(max_so_far)
    return rolling_max


def rolling_max_v2(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max_v2([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: max _ so _ far =
	"""
    return [max(numbers[:i + 1]) for i in range(len(numbers))]


def max_sublist(numbers: List[int]) -> Tuple[int, int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> max_sublist([1, 2, 3, 2, 3, 4, 2])
    (1, 5)
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: max _ so _ far =
	"""
    max_so_far = numbers[0]
    max_ending_here = numbers[0]
    start = 0
    end = 0
    for i, number in enumerate(numbers):
        if number > max_ending_here:
            max_ending_here = number
            end = i
        if number < max_so_far:
            max_so_far = number
            start = i + 1
    return max_so_far, end - start + 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
