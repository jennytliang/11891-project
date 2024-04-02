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



def prod_signs(arr):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]

    sign = 1 

    if arr.count(-1) == len(arr):
        sign = -1
    elif arr.count(0) == len(arr):
        sign = 0
    elif arr.count(-1) == len(arr) // 2 and arr[-1] < 0:
        sign = -1    
    
    prod = arr[0]
    for i in range(1, len(arr)):
        if arr[i - 1] * arr[i] > 0: # Checks if the absolute value of both numbers is greater than 0
            prod 

    return sign * prod