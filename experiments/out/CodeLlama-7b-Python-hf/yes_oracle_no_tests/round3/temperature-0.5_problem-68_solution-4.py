def pluck(arr):
    """
    "Given an array representing a branch of a tree that has non-negative integer nodes
    your task is to pluck one of the nodes and return it.
    The plucked node should be the node with the smallest even value.
    If multiple nodes with the same smallest even value are found return the node that has smallest index.

    The plucked node should be returned in a list, [ smalest_value, its index ],
    If there are no even values or the given array is empty, return [].

    Example 1:
        Input: [4,2,3]
        Output: [2, 1]
        Explanation: 2 has the smallest even value, and 2 has the smallest index.

    Example 2:
        Input: [1,2,3]
        Output: [2, 1]
        Explanation: 2 has the smallest even value, and 2 has the smallest index. 

    Example 3:
        Input: []
        Output: []
    
    Example 4:
        Input: [5, 0, 3, 0, 4, 2]
        Output: [0, 1]
        Explanation: 0 is the smallest value, but  there are two zeros,
                     so we will choose the first zero, which has the smallest index.

    Constraints:
        * 1 <= nodes.length <= 10000
        * 0 <= node.value
    
	Include these tokens in the code: if all ( val %
	"""
    # 1st solution
    # O(n) time | O(n) space
    # def pluck(arr):
    #     if not arr:
    #         return []
    #     nums = {num for num in arr if num % 2 == 0}
    #     if not nums:
    #         return []
    #     return [min(nums), arr.index(min(nums))]

    # 2nd solution
    # O(n) time | O(1) space
    # def pluck(arr):
    #     if not arr:
    #         return []
    #     smallest = min(num for num in arr if num % 2 == 0)
    #     smallest_index = min(i for i, num in enumerate(arr) if num == smallest)
    #     return [smallest, smallest_index]

    # 3rd solution
    # O(n) time | O(1) space
    # def pluck(arr):
    #     if not arr:
    #         return []
    #     smallest = min(num for num in arr if num % 2 == 0)
    #     smallest_index = min(i for i, num in enumerate(arr) if num == smallest)
    #     return [smallest, smallest_index]

    # 4th solution
    # O(n) time | O(1) space
    # def pluck(arr):
    #     if not arr:
    #         return []
    #     smallest = min(num for num in arr if num % 2 == 0)
    #     smallest_index = min(i for i, num in enumerate(arr) if num == smallest)
    #     return [smallest, smallest_index]

    # 5th solution
    # O(n) time | O(1) space
    # def pluck(arr):
    #     if not arr:
    #         return []
    #     smallest = min(num for num in arr if num % 2 == 0)
    #     smallest_index = min(i for i, num in enumerate(