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

    def prod(arr):
        if 0 == len(arr):
            return 1
        elif 1 == len(arr):
            return arr[0]
        else:
            return arr[0] * prod(arr[1:])

    def mag(x):
        return abs(x)

    def sign(x):
        if 0 == x:
            return 0
        elif 0 < x:
            return 1
        else:
            return -1

    return prod(map(mag, arr)) * sign(prod(map(sign, arr)))


# My solution


def prod_signs_2(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs_2([1, 2, 2, -4]) == -9
    >>> prod_signs_2([0, 1]) == 0
    >>> prod_signs_2([]) == None
    
	Include these tokens in the code: arr
	Do not include these tokens in the code: len ( )
	"""

    if len(arr) == 0:
        return None

    def prod(arr):
        if len(arr) == 0:
            return 1
        elif len(arr) == 1:
            return arr[0]
        else:
            return arr[0] * prod(arr[1:])

    def mag(x):
        if x == 0:
            return 0
        elif x > 0:
            return x
        else:
            return -x

    def sign(x):
        if x == 0:
            return 0
        elif x > 0:
            return 1
        else:
            return -1

    return prod(map(mag, arr)) * sign(prod