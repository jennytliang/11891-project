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
    """
    arr.sort()
    return [] if len(arr) == 0 else [
        # return [arr.pop(arr.index(v)), arr.index(v)]
        arr.pop()
        # return min([v, a.pop()])
    ] if len([v for v in arr if v%2 == 0]) and len(arr) else [] 
    """
    This problem isn't really about the tree structure itself.
    If I had been told you need to take an arbitrary value that is inside a tree structure that I will not be provided
    as an argument but I will know about the tree (it has a certain value that need to take) 
    I probably would think about using recursion.
    """
    # return [value, index(n)]

if __name__ == '__main__':
    # Example 1
    print('1: ',pluck([5,1,2,3,2,3,1])) # [3,3] (113) -> [2,0], 110 (4,30)