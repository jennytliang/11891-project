from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: num _ cnt = dict ()
	"""
    num_cnt = {}
    for num in numbers:
        num_cnt[num] = num_cnt.get(num, 0) + 1

    res = []
    for num, cnt in num_cnt.items():
        if cnt == 1:
            res.append(num)
    return res


if __name__ == "__main__":
    import doctest

    doctest.testmod()
