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
    
	Do not include these tokens in the code: prod _ of _ sign s =
	"""
    if len(arr) == 0:
        return None
    prod = 1
    sum = 0
    for num in arr:
        prod *= num
        if num == 0:
            sum += 0
        elif num > 0:
            sum += 1
        elif num < 0:
            sum -= 1
    return sum * prod


if __name__ == '__main__':
    print(prod_signs([1, 2, 2, -4]))
    print(prod_signs([0, 1]))
    print(prod_signs([]))
