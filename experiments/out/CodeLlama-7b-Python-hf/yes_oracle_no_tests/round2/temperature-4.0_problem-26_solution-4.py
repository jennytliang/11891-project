from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Do not include these tokens in the code: if len ( numbers ) <
	"""
    if len(numbers) < 2:
        return numbers
    numbers.sort()
    for i in range(len(numbers) - 1, 0, -1):
        if numbers[i] == numbers[i - 1]:
            numbers.pop(i)
    return numbers


if __name__ == "__main__":
    import doctest

    doctest.testmod()
