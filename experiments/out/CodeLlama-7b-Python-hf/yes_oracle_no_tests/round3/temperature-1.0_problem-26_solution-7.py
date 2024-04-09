from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: num
	Do not include these tokens in the code: # BEGIN
	"""
    # BEGIN Remove this comment.
    # BEGIN Remove this comment.
    new_list = []
    for i in range(0, len(numbers)):
        if numbers[i] not in new_list:
            new_list.append(numbers[i])
    return new_list
    # END Remove this comment.
    # END Remove this comment.


if __name__ == "__main__":
    import doctest

    doctest.testmod()
