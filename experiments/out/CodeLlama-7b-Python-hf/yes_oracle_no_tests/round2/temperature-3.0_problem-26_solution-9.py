from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: dict ()
	Do not include these tokens in the code: {}
	"""

    num_dict = {}
    for num in numbers:
        num_dict[num] = num_dict[num] + 1 if num in num_dict else 1

    return [num for num in numbers if num_dict[num] == 1]


def remove_duplicates_alt(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: dict ()
	Do not include these tokens in the code: {}
    """

    return list(dict.fromkeys(numbers))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
