from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: if number not in num _ cnt :
	"""


    num_cnt = dict()
  
    for number in numbers:
        if number not in num_cnt:
            num_cnt[number] = 1
        else:
            num_cnt[number] += 1

    return [number for number in numbers if num_cnt[number] == 1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
