from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: num _ cnt
	Do not include these tokens in the code: seen
	"""
    # Your implementation here
    i, seen_numbers = 0, set()
    while i < len(numbers):
        num, cnt = numbers[i], 0
        for el in numbers:
            if num == el:
                cnt += 1
        if cnt == 1:
            seen_numbers.add(num)
        i += 1
    
    return sorted(seen_numbers)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
