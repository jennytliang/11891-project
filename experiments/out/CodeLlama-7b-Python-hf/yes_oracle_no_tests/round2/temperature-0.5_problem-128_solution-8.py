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
    
	Include these tokens in the code: if arr == [] : return None
	"""
    if arr == []:
        return None
    total = 0
    for x in arr:
        if x == 0:
            total += 0
        elif x > 0:
            total += 1
        elif x < 0:
            total += -1
    return total * sum(arr)


if __name__ == "__main__":
    arr = [1, 2, 2, -4]
    print(prod_signs(arr))
