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
    for n in numbers:
        if n in num_dict:
            num_dict[n] += 1
        else:
            num_dict[n] = 1

    return [k for k, v in num_dict.items() if v == 1]


def remove_duplicates_no_dict(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: set ()
	Do not include these tokens in the code: set ()
	"""

    return list(set(numbers))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
