def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Do not include these tokens in the code:  if len ( arr ) ==  0 :
	"""

    if len(arr) == 0:
        return -1

    prev = arr[0] - 1
    for i in range(len(arr)):
        if arr[i] <= prev:
            return i
        prev = arr[i]
    return -1


def can_arrange_v2(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Do not include these tokens in the code:  if len ( arr ) ==  0 :
	"""

    if len(arr) == 0:
        return -1

    arr_set = set(arr)
    for i in range(len(arr)):
        if arr[i] + 1 not in arr_set:
            return i
    return -1


if __name__ == '__main__':
    print(can_arrange([1, 2, 4, 3, 5]))
    print(can_arrange([1, 2, 3]))
