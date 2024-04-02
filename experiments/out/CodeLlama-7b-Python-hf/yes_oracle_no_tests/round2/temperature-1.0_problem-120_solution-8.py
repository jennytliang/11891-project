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
    
	Do not include these tokens in the code: 0
	"""

    return sorted(sorted(arr)[:k], reverse=True)

def minimum(arr, k):
    """
    Given an array arr with integers and a positive integer k, you can choose
    exactly k of the integers from the array to form an arithmetic sequence.
    
    An integer sequence is called arithmetic if the consecutive elements have 
    arithmetic distances between them. The distance between the kth and k
    - 1st element in an arithmetic sequence may be a positive, negative, or 
    even distance between them. The n-th element in an arithmetic sequence is
    the sum of the i-th element and a constant delta, where delta is equal 
    to the difference between the k-th and the (k-1)-th elements in the same 
    sequence. The arithmetic sequence containing the  elements should  be 
    monotonically increasing or decreasing. After choosing the set of integers,
    you should return a list of the length k corresponding to the index where 
    each element in the sequence is in the array.

    Note:
        1. If there are multiple ways to choose the k integers that satisfy the 
           conditions in the problem statement, return any answers.

