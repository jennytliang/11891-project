from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Do not include these tokens in the code: # count number of occurr ences of numbers
	"""


    num_cnt = dct = {}
    for num in numbers:
        num_cnt[num] = num_cnt.get(num, 0) + 1

    return [x for x in numbers if num_cnt[x] == 1]



if __name__ == "__main__":
    import doctest
    doctest.testmod()
