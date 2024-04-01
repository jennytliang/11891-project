def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """
    arr_length = len(arr)
    if arr_length <= 1 or is_palindrome(arr, arr_length):
        return 0

    # count the number of occurrences
    counts = {}
    for n in arr:
        if n in counts:
            counts[n] += 1
        else:
            counts[n] = 1

    left_idx = 0
    right_idx = arr_length - 1
    odd_count = 0
    num_changes = 0

    while left_idx < right_idx:
        left = arr[left_idx]
        right = arr[right_idx]

        # left is palindrome
        if left == right:
            left_idx += 1
            continue

        # increment odd counts
        if left not in counts:
            counts[left] = 0
        if right not in counts:
            counts[right] = 0

        counts[left] += 1
        counts[right] += 1

        odd_count += 1
        if odd_count > 1:
            num_changes += 1
        if odd_count > 2:
            num_changes += 2

        left_idx += 1
        right_idx -= 1
