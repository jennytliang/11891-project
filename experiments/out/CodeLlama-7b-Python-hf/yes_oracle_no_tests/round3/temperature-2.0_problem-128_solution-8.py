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
    
	Include these tokens in the code: if 0 in arr : return 0
	Do not include these tokens in the code: elif len ( ) ==
	"""

    if arr == []:
        re = None
    else:
        re = 0
        if 0 in arr:
            re = 0
        else:
            for i in arr:
                if i > 0:
                    re += 1
                elif i < 0:
                    re -= 1
            re = re * sum(arr)
    return re


if __name__ == "__main__":
    print("Example:")
    print(prod_signs([1, 2, 2, -4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert prod_signs([1, 2, 2, -4]) == -9, "Example"
    assert prod_signs([0, 1]) == 0, "Zero"
    assert prod_signs([]) == None, "Empty"
    print("Coding complete? Click 'Check' to earn cool rewards!")
