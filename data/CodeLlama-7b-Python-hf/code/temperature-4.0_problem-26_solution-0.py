from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    if len(numbers) < 2 or len(numbers) > 10e5:
        return "Wrong data format, try again"
    if not numbers:
        return "Empty list"

    seen = dict()
    for i, a in enumerate(numbers):
        if seen.get(a, 0) < 1:
            for x in seen.items():
                if a == x[0]:
                    seen[x[0]] += 1
            seen[a] = 1
            numbers[i] = a
    new_numbers = [str(i) for i, num in enumerate(numbers) if num not in seen]
    return new_numbers
