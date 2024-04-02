from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: num _ cnt
	Do not include these tokens in the code: count
	"""

    # if statement to take care of empty lists
    if not numbers:
        return []

    seen = set()

    seen.add(numbers[0])

    # loop through and add all the items to seen set
    for i in range(1, len(numbers)):
        num = numbers[i]

        if num not in seen:
            seen.add(num)
        else:
            numbers.pop(i)

    return numbers

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(remove_duplicates([1, 2, 3, 2, 4]))
    