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
    
	Include these tokens in the code: if arr == [] : return None if
	"""
    check = lambda x : x if x != 0 else 1
    sign_check = lambda x : x if x > 0 else -1
    if arr == []:
        return None
    else:
        return sum([check(i) for i in arr]) * sign_check(product(prod_pos_neg(arr)))
    

def prod_pos_neg(arr):
    pos_nums = []
    neg_nums = []
    for x in arr:
        if x >= 1:
            pos_nums.append(1)
        elif x <= -1:
            neg_nums.append(-1)
    check = lambda x: x if x!= 0 else 1
    return [check(x) for x in pos_nums + neg_nums]
        
def product(arr):
    return 1 if len(arr) == 1 else reduce(lambda x, y: x*y, arr)

if __name__ == '__main__':
    import doctest
    doctest.testmod(globs=globals())
