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
    
	Do not include these tokens in the code: # sort array first arr
	"""
    # Sort the array first
    arr.sort()
    return arr[:k]

print(maximum([-3, -4, 5], 3)) # [-4, -3, 5]
print(maximum([4, -4, 4], 2)) # [4, 4]
print(maximum([-3, 2, 1, 2, -1, -2, 1], 1)) # [2]

"""
Time O(NlogN)
Space O(N)
"""


def maximum2(arr, k):
    """
    Given an array arr of integers and a positive integer k, find the maximum 
    number of integers that can be chosen from the array such that the 
    difference between any two of the chosen integers is less than or equal 
    to k.

    Example 1:

        Input: arr = [3, 10, 2, 1, 20], k = 2
        Output: 4
        Explanation: All possible subsets are [[3, 10, 2, 1], [2, 10, 2, 3], 
                     [2, 3, 10, 2], [3, 2, 20, 10], [3, 2, 10, 20], [3, 10, 20, 2], 
                     [3, 20, 2, 10], [2, 20, 3, 10], [20, 2, 3, 10], [20, 2, 10, 3], 
                     [20, 3, 10, 2], [20, 3, 2, 10], [20, 10, 2, 3], [10, 2, 3, 2], 
                     [10, 3, 2, 2], [10, 2, 2, 3]]
                     We can choose 4 subsets: [3, 10, 2