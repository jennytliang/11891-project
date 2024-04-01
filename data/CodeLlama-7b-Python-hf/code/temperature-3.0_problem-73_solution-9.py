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
    result = 0
    left, right = 0, len(arr) - 1
    while left < right:
        if arr[left] == arr[right]:
            left += 1
            right -= 1
        elif arr[left] != arr[right] and arr[left] == arr[right - 1]:
            arr[left] = arr[right]
            left += 1
            result += 1
        elif arr[left] != arr[right] and arr[left + 1] == arr[right]:
            arr[left + 1] = arr[right]
            right -= 1
            result += 1
    return result

print(smallest_change)