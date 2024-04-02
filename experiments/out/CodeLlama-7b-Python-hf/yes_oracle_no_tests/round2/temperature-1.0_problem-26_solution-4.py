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
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1
    
    return [ num for num in numbers if num_dict[num] == 1 ]


# Pybites solution

def remove_duplicates1(numbers):
    """Remove duplicates without building a new list.
    >>> remove_duplicates([1, 1, 2])
    [1, 2]
    """

    for i in range(len(numbers) - 1):
        last = i
        next = i + 1

        while (numbers[last] == numbers[next]):
            last += 1
            if (numbers[last] != numbers[next]):
                break
            next += 1
        numbers[last+1:] = numbers[next:]