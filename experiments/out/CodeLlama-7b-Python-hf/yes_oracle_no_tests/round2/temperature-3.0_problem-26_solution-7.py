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
        if num not in num_dict.keys():
            num_dict[num] = 1
        else:
            num_dict[num] += 1

    return [num for num in numbers if num_dict[num] == 1]


def remove_duplicates_no_dict(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: set()
	Do not include these tokens in the code: {}
    """

    return list(set(numbers))


def remove_duplicates_no_set(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: for loop
	Do not include these tokens in the code: {}
    """

    final_list = []
    for num in numbers:
        if num not in final_list:
            final_list.append(num)
    return final_list


if __name__ == "__main__":
    import doctest

    doctest.testmod()
