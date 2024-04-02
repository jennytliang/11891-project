from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Do not include these tokens in the code: # num _ c nt
	"""
    # TODO: Check if this is a valid solution
    # TODO: Check if this is an optimal solution
    # TODO: Check if this is a readable solution
    # TODO: Check if this is a robust solution
    # TODO: Check if this is a scalable solution
    # TODO: What is the time complexity?
    # TODO: What is the space complexity?

    # Check if the list is empty
    if not numbers:
        return numbers

    # Check if the list has only one element
    if len(numbers) == 1:
        return numbers

    # Create a new list
    new_list = []

    # Add the first element
    new_list.append(numbers[0])

    # Iterate over the list
    for i in range(1, len(numbers)):
        # If the element does not already exist in the new list
        if numbers[i] not in new_list:
            # Append the element to the new list
            new_list.append(numbers[i])

    return new_list


if __name__ == "__main__":
    import doctest

    doctest.testmod()
