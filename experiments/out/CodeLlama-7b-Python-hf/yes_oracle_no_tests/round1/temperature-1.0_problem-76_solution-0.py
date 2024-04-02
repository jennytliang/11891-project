def is_simple_power(x, n):
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    
	Include these tokens in the code: if x ==
	"""
    assert (x >=0 and n>0) or (x>0 and n<0),  "Only positive or only negative numbers"
    if x == float("inf"):
      return True
    for a in range(2, (x // n) + 1):
      if x == n**a:
        return True
    return False