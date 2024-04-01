def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    
	Include these tokens in the code: arr _ re vers ed
	Do not include these tokens in the code: # convert to a string
	"""
    # The array is palindrome if it's the same array reversed
    if is_palindrome(arr):
        return 0

    # The array is not palindrome, so we need to make the smallest
    # changes possible to make it palindrome
    re_arr = reverse_array(arr)
    return smallest_changes_to_palindrome(arr, re_arr)


def smallest_changes_to_palindrome(arr, re_arr):
    # The idea is to compare each element in the array with it's
    # corresponding element in the reversed array
    # If the element is the same, we don't need to do any changes
    # If the element is different, we need to make one change
    # If the element is different, we need to count it
    # The number of changes is the sum of the number of differences
    # We can get the number of differences by counting the number of
    # elements that are different between the two arrays
    return sum(1 for a, b in zip(arr, re_arr) if a != b)


def is_palindrome(arr):
    # The array is palindrome if it's the same array reversed
    return arr == reverse_array(arr)


def reverse_array(arr):
    # We need to reverse the array in place, so we can't use the
    # built-in reverse() method
    # We can use a for loop and swap each element in the array
    # with it's corresponding element in the reversed array
    # The reversed array is the same array but reversed
    # We need to count the number of swaps in the array
    # The number of swaps is the length of the array
    # We can use this number to return the number of changes needed
    # to make the array palindrome
    number_of_swaps = len(arr)
    for i in range(number_of_swaps // 2):
        # Swap the ith element with the ith element from the end
        arr[i], arr[~i] = arr[~i], arr[i]
