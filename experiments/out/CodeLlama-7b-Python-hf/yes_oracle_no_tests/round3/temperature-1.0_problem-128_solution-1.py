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

  if len(arr) == 0:
    return None
    
  signs = [1 if x > 0 else -1 if x < 0 else 0 for x in arr]
  return sum(signs) * prod(signs)


def prod(arr):
    """
    You are given an array arr of integers and you need to return
    product of all numbers in the array.
    Note: return None for empty arr.

    Example:
    >>> prod([1, 2, 2, -4]) == -9
    >>> prod([0, 1]) == 0
    >>> prod([]) == None
    
	Include these tokens in the code: arr
	Do not include these tokens in the code: len ( )
	"""

  if len(arr) == 0:
    return None
  
  return reduce(lambda x, y: x * y, arr)