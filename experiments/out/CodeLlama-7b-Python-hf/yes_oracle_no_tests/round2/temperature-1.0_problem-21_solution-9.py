from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    
	Include these tokens in the code: , mi
	"""


def rescale_to_range(numbers: List[float], output_range: tuple[float, float]) -> List[float]:
    current_min, current_max = get_min_and_max(numbers)
    desired_min, desired_max = output_range
    num_diff = max(0.0001, desired_max - desired_min)
    cur_diff = current_max - current_min

    def normalize(n: float) -> float:
        return (cur_diff * (n - current_min) / num_diff) + desired_min

    return list(map(normalize, numbers))


def get_min_and_max(numbers: List[float]) -> tuple[float, float]:
    min_val = float("inf")
    max_val = float("-inf")
    for n in numbers:
        if n < min_val:
            min_val = n

        if n > max_val:
            max_val = n

    return min_val, max_val
