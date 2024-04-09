def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    
	Do not include these tokens in the code: # code goes here
	"""
    # code goes here
    # pass
    if not arr:
        return None
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return arr[0] * arr[1]
    
    # 1. find the first non-zero element
    # 2. if there is no non-zero element, return 0
    # 3. if there is only one non-zero element, return it
    # 4. otherwise, return sum of magnitudes of integers multiplied by product of all signs of each number in the array
    # 5. if there are two non-zero elements, return the product of the two numbers
    
    nonzero_index = None
    for i in range(len(arr)):
        if arr[i] != 0:
            nonzero_index = i
            break
    if nonzero_index == None:
        return 0
    if len(arr) == nonzero_index + 1:
        return arr[nonzero_index]
    if len(arr) == nonzero_index + 2:
        return arr[nonzero_index] * arr[nonzero_index + 1]
    
    prod = 1
    for i in range(len(arr)):
        if arr[i] == 0:
            prod = 0
            break
        if arr[i] < 0:
            prod *= -1
    
    sum = 0
    for i in range(len(arr)):
        sum += abs(arr[i])
    
    return sum * prod

if __name__ == '__main__':
    import doctest
    doctest.testmod()
