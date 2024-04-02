def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    
	Include these tokens in the code: arr _ re vers
	Do not include these tokens in the code: # create a revers
	"""
    # Find the number of elements in the array
    n = len(arr)
    
    # Find the number of elements in the middle of the array
    middle = n // 2
    
    # Create a list to store the values of the array
    new_arr = []
    
    # Add the first half of the array to the list
    for i in range(middle):
        new_arr.append(arr[i])
    
    # If the array is odd, add the last element to the list
    if n % 2 != 0:
        new_arr.append(arr[-1])
    
    # Reverse the list
    new_arr.reverse()
    
    # Find the number of changes needed
    changes = 0
    
    # Iterate through the lists
    for i in range(len(new_arr)):
        if new_arr[i] != arr[i]:
            changes += 1
    
    return changes


print(smallest_change([1, 2, 3, 5, 4, 7, 9, 6]))
print(smallest_change([1, 2, 3, 4, 3, 2, 2]))
print(smallest_change([1, 2, 3, 2, 1]))