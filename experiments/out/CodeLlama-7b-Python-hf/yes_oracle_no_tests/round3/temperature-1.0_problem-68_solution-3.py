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
    # 1. Brute-force: O(n)
    # 2. Optimize: O(n)
    # 3. Brute-force: O(n)
    # 4. Optimize: O(n)
    # 5. Brute-force: O(n)
    # 6. Optimize: O(n)
    # 7. Brute-force: O(n)
    # 8. Optimize: O(n)
    # 9. Brute-force: O(n)
    # 10. Optimize: O(n)
    # 11. Brute-force: O(n)
    # 12. Optimize: O(n)
    # 13. Brute-force: O(n)
    # 14. Optimize: O(n)
    # 15. Brute-force: O(n)
    # 16. Optimize: O(n)
    # 17. Brute-force: O(n)
    # 18. Optimize: O(n)
    
    # 1. Brute-force
    # def pluck(arr):
    #     if arr == []:
    #         return []
    #     else:
    #         smallest = min(arr)
    #         if smallest % 2 == 0:
    #             return [smallest, arr.index(smallest)]
    #         else:
    #             return pluck(arr[1:])
    
    # 2. Optimize
    # def pluck(arr):
    #     if arr == []:
    #         return []
    #     elif arr[0] % 2 == 0:
    #         return [arr[0], 0]
    #     else:
    #         return pluck(arr[1:])
    
    # 3. Brute-force
    # def pluck(arr):
    #     if arr == []:
    #         return []
    #     else:
    #         smallest =