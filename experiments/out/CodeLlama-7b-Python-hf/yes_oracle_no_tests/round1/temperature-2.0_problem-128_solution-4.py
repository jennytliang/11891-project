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

  sum = 0
  for i in arr:
    if i > 0:
      sum += 1
    elif i == 0:
      sum += 0
    else:
      sum -= 1
  if sum == 0:
    return 0
  else:
    return sum * (-1) * (arr[0])


print(prod_signs([1, 2, 2, -4]))
print(prod_signs([0, 1]))
print(prod_signs([]))
