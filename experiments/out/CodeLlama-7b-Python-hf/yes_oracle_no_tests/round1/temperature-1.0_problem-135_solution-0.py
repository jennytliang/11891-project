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
    def can_arrange(n, m, arr):
        if n <= m:
            return m
        return min(can_arrange(n, k, arr) for k in range(m) if arr[k] <= n)
    return can_arrange(max(arr), 0, arr)

print(can_arrange([1,2,4,3,5]))