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
    
	Include these tokens in the code: arr
	Do not include these tokens in the code: len ( )
	"""

    if 0 == len(arr):
        return None
    else:
        # Multiply all the numbers in the list
        prod = arr[0]
        for i in range(1, len(arr)):
            prod *= arr[i]

        # Multiply all the signs in the list
        signs = 1
        for i in range(len(arr)):
            if arr[i] < 0:
                signs *= -1
            else:
                signs *= 1

        return signs * prod

print(prod_signs([1, 2, 2, -4]))
print(prod_signs([0, 1]))
print(prod_signs([]))
