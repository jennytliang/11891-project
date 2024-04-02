from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    
	Include these tokens in the code: ma , mi
	Do not include these tokens in the code: min _ number
	"""
    minimum = min(numbers)
    maximum = max(numbers)
    if max == minimum:
        max = minimum + 1
    return [(x - minimum) / (maximum - minimum) for x in numbers]


def get_min_max(numbers: List[float]) -> List[float]:
    """
	Define two variables min_v and max_v to be minimum and maximum values of the incoming List numList
	Return the min_v and max_v in a List
	Your code here
	
	Include these tokens in the code:
	
	    len(numbers), min(numbers, numbers[0], max(numbers, number[0]), numberList
	    _ v, _ v
	"""
    minimum = min(numbers)
    maximum = max(numbers)
    return [minimum, maximum]


# test code
numbers = [1.0, 2.0, 32.0, 4.0, 5.0]
print(get_min_max(numbers))
print(rescale_to_unit(numbers))
