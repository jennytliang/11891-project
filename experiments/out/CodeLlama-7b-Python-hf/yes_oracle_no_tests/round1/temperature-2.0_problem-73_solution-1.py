def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    
	Include these tokens in the code: arr _ re vers ed , c nt = arr
	Do not include these tokens in the code: if len ( ) <
	"""
    # first, we'll make a copy of the array and reverse it. Then, if we iterate through the array, 
    # we can compare the reverse and non-reverse array at the same index, and increment a variable 
    # called "changes" if the values are different. 
    # Then, we return the minimum of the length of the array and the "changes" variable.
    arr_reversed = arr[::-1]
    changes = 0
    for i in range(len(arr)):
        if arr[i] != arr_reversed[i]:
            changes += 1
    return min(len(arr), changes)

print(smallest_change([1,2,3,5,4,7,9,6]))
print(smallest_change([1, 2, 3, 4, 3, 2, 2]))
print(smallest_change([1, 2, 3, 2, 1]))

# Complexity: Time O(n) | Space O(n)

# Time O(n)
# We iterate through the array once, so time complexity is O(n).

# Space O(n)
# The array that we return is the same size as the original array, so space complexity is O(n).

# Can we do better?
# No. If we iterate through the array, we're going to have to compare the values of the array at the same index.
# If the values are different, we'll increment a variable called "changes".
# Then, we'll have to return the minimum of the length of the array and the "changes" variable.
# If we don't iterate through the array, we won't be able to count the number of changes.
# If we don't return the minimum of the length and changes, we won't be able to return the minimum number of changes.
# So, time and space complexity are O(n).