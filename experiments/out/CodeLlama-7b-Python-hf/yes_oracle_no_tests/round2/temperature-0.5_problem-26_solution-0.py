from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: num _ cnt
	Do not include these tokens in the code: seen
	"""
    seen = set()
    nums = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            nums.append(num)
    return nums


def test_remove_duplicates():
    assert remove_duplicates([1, 2, 3, 2, 4]) == [1, 3, 4]
    assert remove_duplicates([1, 2, 2, 2, 4, 5, 6, 6, 7, 8, 9]) == [1, 4, 5, 7, 8, 9]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
