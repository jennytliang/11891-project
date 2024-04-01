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
    elif len(arr) == 1:
        return arr[0]
    else:
        negative = 0
        positive = 0
        zero = 0
        for i in range(len(arr)):
            if arr[i] < 0:
                negative += 1
            elif arr[i] == 0:
                zero += 1
            else:
                positive += 1
        
        if negative == 0 or positive == 0:
            return 0
        else:
            return ((positive - negative) * (negative * positive))

print(prod_signs([1, 2, 2, -4]))
print(prod_signs([0, 1]))
print(prod_signs([]))