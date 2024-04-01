def get_odd_collatz(n):
    """
    Given a positive integer n, return a sorted list that has the odd numbers in collatz sequence.

    The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined
    as follows: start with any positive integer n. Then each term is obtained from the 
    previous term as follows: if the previous term is even, the next term is one half of 
    the previous term. If the previous term is odd, the next term is 3 times the previous
    term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.

    Note: 
        1. Collatz(1) is [1].
        2. returned list sorted in increasing order.

    For example:
    get_odd_collatz(5) returns [1, 5] # The collatz sequence for 5 is [5, 16, 8, 4, 2, 1], so the odd numbers are only 1, and 5.
    
	Include these tokens in the code: ,
	Do not include these tokens in the code: = [ 1 ]
	"""


  ########################################################################################
  # Get odd collatz sequence
  #
  # @param n the input number
  # @return the list of odd numbers in the collatz sequence for n
  # @raise Exception if n is not a positive integer
  def get_odd_collatz(n):
    if (n % 1) == 0:
      if n < 1:
        raise Exception("n is not a positive integer")
      else:
        return _get_odd_collatz(n)
    else:
      raise Exception("n is not a positive integer")


  ########################################################################################
  # Get odd collatz sequence
  #
  # @param n the input number
  # @return the list of odd numbers in the collatz sequence for n
  def _get_odd_collatz(n):
    if n == 1:
      return [1]
    elif n % 2 == 0:
      return _get_odd_collatz(n / 2) + [n]
    else:
      return _get_odd_collatz((3 * n) + 1) + [n]
