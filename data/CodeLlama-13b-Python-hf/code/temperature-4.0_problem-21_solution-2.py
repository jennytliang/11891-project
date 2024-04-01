from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    assert (
        _check_at_least_two_items(numbers)
        and "List must have at least two elements"
    )
    return [_calculate_scaling(num) for num in numbers]


def _check_at_least_two_items(numbers: List[float]) -> bool:
    return len(numbers) > 1


def _calculate_diff(numbers: List[float]) -> int:
    return max(numbers) - min(numbers)

def _calculate_offset(numbers: List[float])->int:
    return min(min(numbers) + 1, (min(numbers) + max(numbers)) / 2)


def _calculate_scaling(_offset: int) -> int: return (1)