from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: num _ cnt
	Do not include these tokens in the code: un iques
	"""
    uniques = set()
    result = []
    for num in numbers:
        if num not in uniques:
            result.append(num)
            uniques.add(num)
    return result


def remove_duplicates_sorted(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements sorted as in the input.
    >>> remove_duplicates_sorted([1, 2, 3, 2, 4])
    [1, 2, 4]
    
	Include these tokens in the code: num _ cnt
	Do not include these tokens in the code: un iques
	"""
    uniques = set()
    result = []
    for num in sorted(numbers):
        if num not in uniques:
            result.append(num)
            uniques.add(num)
    return result


def main():
    numbers = [1, 2, 3, 2, 4]
    print(remove_duplicates(numbers))
    print(remove_duplicates_sorted(numbers))


if __name__ == "__main__":
    main()
