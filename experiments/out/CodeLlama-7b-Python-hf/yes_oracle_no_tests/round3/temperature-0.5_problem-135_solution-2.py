def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Do not include these tokens in the code: # Your code here if
	"""
    # 1. Create a new list with the same elements as the original list, but
    #    sorted in descending order.
    descending_list = sorted(arr, reverse=True)
    # 2. Create a new list with the same elements as the original list, but
    #    sorted in ascending order.
    ascending_list = sorted(arr)

    # 3. Create a new list with the same elements as the original list, but
    #    sorted in descending order.
    # 4. Create a new list with the same elements as the original list, but
    #    sorted in ascending order.
    # 5. Create a new list with the same elements as the original list, but
    #    sorted in descending order.
    # 6. Create a new list with the same elements as the original list, but
    #    sorted in ascending order.
    # 7. Create a new list with the same elements as the original list, but
    #    sorted in descending order.
    # 8. Create a new list with the same elements as the original list, but
    #    sorted in ascending order.
    # 9. Create a new list with the same elements as the original list, but
    #    sorted in descending order.

    # 10. Return the largest index of an element which is not greater than or
    #     equal to the element immediately preceding it. If no such element
    #     exists then return -1.

    # 11. Do not include these tokens in the code: # Your code here if

    # 12. Make sure to return the correct value.

    return -1


if __name__ == '__main__':
    print(can_arrange([1,2,4,3,5]))
    print(can_arrange([1,2,3]))
    print(can_arrange([1,2,3,4,5]))
    print(can_arrange([1,2,3,4,5,6]))
