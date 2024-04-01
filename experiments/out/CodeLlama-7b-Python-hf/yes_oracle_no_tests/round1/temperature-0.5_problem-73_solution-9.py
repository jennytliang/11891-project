def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    
	Include these tokens in the code:  arr _ re vers ed , c nt
	Do not include these tokens in the code: if len
	"""

    # TODO: Write a solution here
    if len(arr) == 0:
        return 0

    # Find the middle of the array
    middle = len(arr) // 2

    # Create the re-ordered array
    new_arr = arr[middle:] + arr[:middle]

    # Get the differences between the two arrays
    diffs = [new_arr[i] - arr[i] for i in range(len(arr))]

    # Return the number of differences
    return sum(map(abs, diffs))


print(smallest_change([1, 2, 3, 5, 4, 7, 9, 6]))
print(smallest_change([1, 2, 3, 4, 3, 2, 2]))
print(smallest_change([1, 2, 3, 2, 1]))
