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
    for n in numbers:
        if n not in cnt:
            cnt[n] = 1
        else:
            cnt[n] += 1
    result = []
    for n in numbers:
        if cnt[n] == 1:
            result.append(n)
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
