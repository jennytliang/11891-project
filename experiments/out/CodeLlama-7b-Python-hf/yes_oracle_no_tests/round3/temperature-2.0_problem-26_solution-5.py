from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: cnt
	Do not include these tokens in the code: dict
	"""


  
    # Create a dictionary and count the occurences of each number
    cnt = {}
    for num in numbers:
        if num in cnt:
            cnt[num] += 1
        else:
            cnt[num] = 1

    # Create a new list to return
    new_list = []

    # Add numbers that occur once to the new list
    for num in numbers:
        if cnt[num] == 1:
            new_list.append(num)

    return new_list



def remove_duplicates_tuple(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: cnt, dict
	Do not include these tokens in the code: list
	"""

    # Create a dictionary and count the occurences of each number
    cnt = {}
    for num in numbers:
        if num in cnt:
            cnt[num] += 1
        else:
            cnt[num] = 1

    # Create a new list to return
    new_list = []

    # Add numbers that occur once to the new list
    for num in numbers:
        if cnt[num] == 1:
            new_list.append(num)

    return new_list



def remove_duplicates_set(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: set
	Do not include these tokens in the code: list, dict
	"""

    # Create a set and add each number only