def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Do not include these tokens in the code: def can _ ar range _ index
	"""

    # can ar range, index
    # O(n) time, n is size of input array
    # O(1) space

    max_val = -1
    arr.append(-1)                  # add tail
    arr.reverse()                   # to easily compute diffs

    for i, val in enumerate(arr):  # traverse in reverse order
        if val < max_val:
            arr[i] = max_val        # update at index
        else:
            max_val = val           # if no match, update max_val

    return arr.index(-1)            # return the index of the tail

if __name__ == "__main__":
    array = [1, 2, 4, 3, 5]
    print(can_arrange(array))
