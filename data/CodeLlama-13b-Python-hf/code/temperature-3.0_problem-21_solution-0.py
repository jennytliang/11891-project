from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # Check for empty input
    if len(numbers) == 0:
        return []
    
    # Check for one element
    if len(numbers) == 1:
        return [0]
    
    # Find min and max
    min_value = min(numbers)
    max_value = max(numbers)
    
    # Find range
    ranges = max_value - min_value
    
    # Return list
    return [(x - min_value)/ranges for x in numbers]
