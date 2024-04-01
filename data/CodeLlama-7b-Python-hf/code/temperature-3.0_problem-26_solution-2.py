from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    if not numbers:
        return numbers
    numbers_unique: List[int] = []
    numbers_unique.append(numbers[0])
    for i in range(1, len(numbers)):
        if numbers[i - 1] != numbers[i]:
            numbers_unique.append(numbers[i])
    return numbers_unique


if __name__ == "__main__":
    import doctest
    doctest.testmod()

