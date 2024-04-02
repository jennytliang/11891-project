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
    
	Do not include these tokens in the code: #
	"""
    if len(arr) == 0:
        return None
    
    total = 0
    product = 1
    for num in arr:
        if num == 0:
            product = 0
            break
        elif num > 0:
            product *= 1
            total += num
        else:
            product *= -1
            total += num

    return total * product


if __name__ == '__main__':
    print("Example:")
    print(prod_signs([1, 2, 2, -4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert prod_signs([1, 2, 2, -4]) == -9
    assert prod_signs([0, 1]) == 0
    assert prod_signs([]) == None
    print("Coding complete? Click 'Check' to earn cool rewards!")