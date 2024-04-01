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
    if len(arr) < 2:
        return 0

    n = len(arr)
    dp = [n] * n
    dp[0] = 0
    dp[1] = 0 if arr[0] == arr[1] else 1

    for i in range(2, n):
        if arr[i] == arr[i - 1]:
            dp[i] = dp[i - 1]
        elif arr[i] == arr[i - 2]:
            dp[i] = dp[i - 2] + 1
        else:
            dp[i] = min(dp[i - 1], dp[i - 2]) + 1

    return dp[n - 1]
