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
    
	Include these tokens in the code: if
	Do not include these tokens in the code: signs = [ 1 , - 1 ,
	"""

    if arr == []:
        re = None
    else:
        signs = [1, -1, 0]
        re = 0
        for i in arr:
            re += signs.index(i / abs(i))
        re = re * arr[-1]
    return re


def test_function():
    assert prod_signs([1, 2, 2, -4]) == -9
    assert prod_signs([0, 1]) == 0
    assert prod_signs([]) is None
    assert prod_signs([1, 0, 2, 3, -4]) == 0
    assert prod_signs([1, 2, 3, -4]) == 0
    assert prod_signs([1, -2, -3, 4]) == 0
    assert prod_signs([-1, -2, -3, -4]) == 0
    assert prod_signs([1, -2, -3, -4]) == 0
    assert prod_signs([1, 2, 3, 4]) == 24
    assert prod_signs([-1, -2, -3, -4]) == 24
    assert prod_signs([-1, 2, 3, -4]) == 24
    assert prod_signs([-1, -2, 3, -4]) == 24
    assert prod_signs([-1, 2, -3, -4]) == 24
    assert prod_signs([1, 2, 3, 4]) == 24
    assert prod_signs([-1, -2, -3, 4]) == 24
    assert prod_signs([1, -2, 3, 4]) == 24
    assert prod_signs([1, -2, -3, 4]) == 24
    assert prod_signs([1, -2, 3, -4]) == 24
    assert prod_signs([1, 2, -3, -4]) == 24
    assert prod_signs([-1,