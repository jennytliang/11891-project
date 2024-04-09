def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    Example 1:

        Input: arr = [-3, -4, 5], k = 3
        Output: [-4, -3, 5]

    Example 2:

        Input: arr = [4, -4, 4], k = 2
        Output: [4, 4]

    Example 3:

        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
        Output: [2]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
        3. 0 <= k <= len(arr)
    
	Do not include these tokens in the code: from collections import C ounter
	"""
    n = len(arr)
    if n <= k:
        return sorted(arr)
    freq = [0] * 1001
    for i in range(n):
        freq[arr[i] + 1000] += 1
    ans = []
    for i in range(1000, -1, -1):
        if freq[i] > 0:
            ans.append(i - 1000)
            freq[i + 1] -= 1
            freq[i] -= 1
            if len(ans) == k:
                return ans
    return ans


if __name__ == "__main__":
    arr = [-3, -4, 5]
    k = 3
    print(maximum(arr, k))
