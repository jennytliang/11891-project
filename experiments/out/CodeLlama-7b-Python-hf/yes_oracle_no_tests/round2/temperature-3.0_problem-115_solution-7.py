import math

def max_fill(grid, capacity):
    """
    You are given a rectangular grid of wells. Each row represents a single well,
    and each 1 in a row represents a single unit of water.
    Each well has a corresponding bucket that can be used to extract water from it, 
    and all buckets have the same capacity.
    Your task is to use the buckets to empty the wells.
    Output the number of times you need to lower the buckets.

    Example 1:
        Input: 
            grid : [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
            bucket_capacity : 1
        Output: 6

    Example 2:
        Input: 
            grid : [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
            bucket_capacity : 2
        Output: 5
    
    Example 3:
        Input: 
            grid : [[0,0,0], [0,0,0]]
            bucket_capacity : 5
        Output: 0

    Constraints:
        * all wells have the same length
        * 1 <= grid.length <= 10^2
        * 1 <= grid[:,1].length <= 10^2
        * grid[i][j] -> 0 | 1
        * 1 <= capacity <= 10
    
	Include these tokens in the code: ans =
	"""
    def bucket_fill(grid, capacity):
        # TODO: Write your code here
        pass

    return bucket_fill(grid, capacity)


def max_sum_increasing_subsequence(arr):
    """
    Given an array of integers arr, find the maximum sum of an increasing subsequence in arr and return it.
    A subsequence of an array arr is a new array obtained by deleting some (possibly, none or all) elements of arr.

    Example 1:
        Input: arr = [10,20,30,5,10,50]
        Output: 75
        Explanation: The optimal increasing sequence is [10,20,30,50] with a sum of 75.

    Example 2:
        Input: arr = [1,2,3,4,5,6]
        Output: 21
        Explanation: The optimal increasing sequence is [1,2,3,4,5,6] with a sum of 21.

    Example 3:
        Input: arr = [1,5,10,5,16,20]
        Output: 41
        Explanation: The optimal increasing sequence is [1,5,10,16,20] with a sum of 41.

    Constraints:
        * 1 <= arr.length <= 10^5
        * 1 <= arr[i] <= 10^6
    
    Include these tokens in the code: ans =
    """
    def max_sum_increasing_subsequence(arr):
        # TODO: Write your code here
        pass

    return max_sum_increasing_subsequence(arr)


def max_sum_subarray(arr):
    """
    Given an array of integers arr, find the maximum sum of a non-empty subarray of arr.
    You may assume that arr[i] is an integer between -100,000 and 100,000.

    Example 1:
        Input: arr = [-2,1,-