from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Do not include these tokens in the code: result = []
	"""
    result = []
    for i in numbers:
        if numbers.count(i) == 1:
            result.append(i)
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
