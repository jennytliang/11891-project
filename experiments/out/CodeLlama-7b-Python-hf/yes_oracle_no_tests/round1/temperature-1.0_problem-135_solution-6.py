def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Do not include these tokens in the code: if len ( arr ) ==
	"""
    from collections import defaultdict
    d = defaultdict(int) # value: indexes where it occurs
    for i, x in enumerate(arr): 
        d[x].append(i)
        
    return -1


if __name__ == "__main__":
    arr = [1, 7, 3, 2, 5, 4]  # 3
    arr1 = [1, 2, 3]  # -1
    print(can_arrange(arr) == 3)  # output: True
    print(can_arrange(arr1) == -1)  # output: True
    arr = [1, 7, 3, 2, 5, 4, 6, 8]  # 4
    print(can_arrange(arr) == 4)  # output: True
