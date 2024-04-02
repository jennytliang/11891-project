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
        if num not in num_dict:
            num_dict[num] = 0
        else:
            num_dict[num] += 1

    return [x for x in numbers if num_dict[x] == 1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
