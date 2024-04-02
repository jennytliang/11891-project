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

  # if len(arr) == 0:
  #   return None
  # else:
  #   return sum(arr) * product(arr)
  return sum(arr) * product(arr) if arr else None


def product(arr):
    """
    You are given an array arr of integers and you need to return
    product of all numbers multiplied by product of all signs of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> product([1, 2, 2, -4]) == 9
    >>> product([0, 1]) == 0
    >>> product([]) == None
    
	Include these tokens in the code: arr
	Do not include these tokens in the code: len ( )
	"""

  # if len(arr) == 0:
  #   return None
  # else:
  #   return product([x if x != 0 else 1 for x in arr])
  return product([x if x != 0 else 1 for x in arr]) if arr else None



def prod_signs_2(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs_2([1, 2, 2, -4]) == -9
    >>> prod_signs_2([0, 1]) == 0
    >>> prod_signs_2([]) == None
    
	Include these tokens in the code: arr
	Do not include these tokens in the code: len ( )
	"""

  # if len(arr) == 0:
  #   return None
  # else:
  #   return sum(arr) * product(arr)
  return sum(arr) * product(arr) if arr else None


def product_2(arr):
    """
    You are given an array