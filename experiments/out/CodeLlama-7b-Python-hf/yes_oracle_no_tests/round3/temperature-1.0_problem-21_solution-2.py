from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    
	Include these tokens in the code: , mi
	"""

  # This is my solution
    min_num = min(numbers)
    max_num = max(numbers)
    result = []
    for num in numbers:
        result.append((num - min_num) / (max_num - min_num))
    return result


# This is the solution my instructor provided
# def rescale_to_unit(numbers: List[float]) -> List[float]:
#     """ Given list of numbers (of at least two elements), apply a linear transform to that list,
#     such that the smallest number will become 0 and the largest will become 1
#     >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
#     [0.0, 0.25, 0.5, 0.75, 1.0]
#     """

#     # This is my solution
#     min_num = min(numbers)
#     max_num = max(numbers)
#     result = []
#     for num in numbers:
#         result.append((num - min_num) / (max_num - min_num))
#     return result


# This is the solution my TA provided
# def rescale_to_unit(numbers: List[float]) -> List[float]:
#     """ Given list of numbers (of at least two elements), apply a linear transform to that list,
#     such that the smallest number will become 0 and the largest will become 1
#     >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
#     [0.0, 0.25, 0.5, 0.75, 1.0]
#     """

#     # This is my solution
#     min_num = min(numbers)
#     max_num = max(numbers)
#     result = []
#     for num in numbers:
#         result.append((num - min_num) / (max_num - min_num))
#     return