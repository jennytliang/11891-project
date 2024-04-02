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
    
	Do not include these tokens in the code: n == 1 and
	"""

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # Explanation
  #
  # This problem is a simple matter of finding the base and exponent of a number.
  # We know that any number is a power of n if n ** exponent = number
  #
  # The first step is to find the exponent. We can do this by taking the
  # logarithm of the number to the base of n. If the number is a power of n,
  # then the exponent must be a whole number. We can round the number to
  # find the exponent.
  #
  # The second step is to find the base. We can do this by dividing the number
  # by the exponent.
  #
  # The third step is to confirm that the base is equal to n.
  #
  # If the number is a power of n, then exponent will be a whole number, the
  # base will be equal to n, and the number will be the same as the number
  # we started with.
  #
  # If the number is not a power of n, then the exponent will be a decimal,
  # the base will not be equal to n, or the number will not be the same as
  # the number we started with.
  #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # Pseudocode
  #
  # 1. Find the exponent
  # 2. Find the base
  # 3. Confirm that the base is equal to n
  #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # Complexity
  #
  # Time complexity: O(1)
  # Space complexity: O(1)
  #
  # # # # # # # # # # # # # # # # # # # # #