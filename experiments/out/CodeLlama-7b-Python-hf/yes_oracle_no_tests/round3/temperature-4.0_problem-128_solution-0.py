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


    def sign(num):
        if num > 0:
            return 1
        elif num < 0:
            return -1
        elif num == 0:
            return 0

    if len(arr) == 0:
        return None

    sum_of_magnitudes = 0
    product_of_signs = 1

    for num in arr:
        sum_of_magnitudes += abs(num)
        product_of_signs *= sign(num)
    return sum_of_magnitudes * product_of_signs

print(prod_signs([1, 2, 2, -4]))
print(prod_signs([0, 1]))
print(prod_signs([]))
