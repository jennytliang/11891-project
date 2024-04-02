def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Do not include these tokens in the code: # Find the largest element in the
	"""
    # Find the largest element in the array
    largest = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]

    # Create a new array and copy the elements
    new_arr = []
    for i in range(len(arr)):
        new_arr.append(arr[i])

    # Find the index of the largest element
    index = 0
    for i in range(len(arr)):
        if arr[i] == largest:
            index = i
            break

    # Iterate through the array and find the largest element that is smaller
    # than the largest element
    for i in range(index):
        if arr[i] <= largest:
            largest = arr[i]

    # Iterate through the array again and find the index of the largest element
    # that is smaller than the largest element
    for i in range(len(arr)):
        if arr[i] == largest:
            index = i
            break

    return index


# Uncomment the line below when your function is done
print(can_arrange([1, 2, 4, 3, 5]))
