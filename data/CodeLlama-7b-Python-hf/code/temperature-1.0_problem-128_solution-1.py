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
    """
    if len(arr) == 0:
        return None
    elif len(arr) == 1:
        if arr[0] > 0:
            return arr[0]
        elif arr[0] < 0:
            return -arr[0]
        else:
            return 0
    elif len(arr) == 2:
        if arr[0] > 0 and arr[1] > 0:
            return arr[0] * arr[1]
        elif arr[0] > 0 and arr[1] < 0:
            return -arr[0] * arr[1]
        elif arr[0] < 0 and arr[1] > 0:
            return -arr[0] * arr[1]
        elif arr[0] < 0 and arr[1] < 0:
            return arr[0] * arr[1]
    else:
        if arr[0] > 0:
            return arr[0] * prod_signs(arr[1:])
        elif arr[0] < 0:
            return -arr[0] * prod_signs(arr[1:])
        else:
            return 0 * prod_signs(arr[1:])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
