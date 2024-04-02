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

  return None

  # My first solution but it fails
  # return np.sign(prod(array) * sum([item for item in arr if item != 0]))
  # return np.sign(array)


# TESTS
# assert prod_signs([1, 2, 2, -4]) == -9
# assert prod_signs([0, 1]) == 0
# assert prod_signs([]) == None

# OWN SOLUTION
# import numpy as np
# def prod_signs(arr):
#   return np.sign(arr) * np.prod(arr)

# import numpy as np

# def prod_signs(arr):
#   return np.multiply.reduce(np.sign(np.array(arr))) * np.prod(np.abs(np.array(arr)))

# def prod_signs(arr):
#   return np.sign(prod(array)) * np.sum(np.abs(array))

# import numpy as np 

# def prod_signs(arr):       
#   if len(arr) == 1 and arr[0] == 0:
#       return 0
#   return np.sign(arr).prod() * np.abs(arr).sum()

# from itertools import chain
# def prod_signs(arr):
#     return signal(map(lambda x: abs(x), chain.from_iterable([sign(x) for x in arr])))

# return list(chain.from_iterable([signal(x) for x in iterable]))

#  from itertools import chain
# def prod_signs(arr):
#     return signal([abs(x) for x in chain(*sign(iterable))])
