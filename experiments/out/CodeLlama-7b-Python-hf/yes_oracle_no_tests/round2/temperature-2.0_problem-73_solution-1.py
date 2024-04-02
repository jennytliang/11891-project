def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    
	Do not include these tokens in the code: # first , we ' ll make
	"""
    # your code here
    if arr == None or len(arr) == 0:
        return

    n = len(arr)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0
    for i in range(n - 1):
        dp[i][i + 1] = 0 if arr[i] == arr[i + 1] else 1
    for i in range(n - 2, -1, -1):
        for j in range(i + 2, n):
            dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1

    return dp[0][-1]


if __name__ == '__main__':
    arr1 = [1, 2, 3, 5, 4, 7, 9, 6]
    arr2 = [1, 2, 3, 4, 3, 2, 2]
    arr3 = [1, 2, 3, 2, 1]
    print(smallest_change(arr1))
    print(smallest_change(arr2))
    print(smallest_change(arr3))
