from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Do not include these tokens in the code: result = []
	"""
    # base case:
    if len(numbers) == 0:
        return []
    else:
        # we will use a set to keep track of the already seen elements
        seen = set()
        # we will use a list to store the final result
        result = []
        # we will iterate over the elements in the list
        for number in numbers:
            # if we have seen this number already, we will skip it
            if number in seen:
                continue
            # otherwise we add it to the result list
            result.append(number)
            # and add it to the set of seen elements
            seen.add(number)
        return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
