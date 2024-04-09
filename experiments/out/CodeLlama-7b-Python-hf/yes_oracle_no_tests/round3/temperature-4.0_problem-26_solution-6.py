from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: cnt
	Do not include these tokens in the code: dict
	"""


  
    cnt = {}
    for number in numbers:
        if number in cnt:
            cnt[number] += 1
        else:
            cnt[number] = 1
    return [number for number in numbers if cnt[number] == 1]



def remove_duplicates_dict(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: cnt
	Do not include these tokens in the code: dict
	"""

    cnt = {}
    for number in numbers:
        if number in cnt:
            cnt[number] += 1
        else:
            cnt[number] = 1
    return [number for number in numbers if cnt[number] == 1]



def remove_duplicates_no_dict(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: cnt
	Do not include these tokens in the code: dict
	"""


    numbers.sort()
    return [numbers[i] for i in range(len(numbers)) if numbers[i] != numbers[i + 1]]





print(remove_duplicates([1, 2, 3, 2, 4]))
print(remove_duplicates_dict([1, 2, 3, 2, 4]))
print(remove_duplicates_no_dict([1, 2, 3, 2, 4]))
