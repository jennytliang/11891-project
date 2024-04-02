def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    
	Do not include these tokens in the code: # 1 .
	"""
    # BEGIN PROBLEM 1
    if len(l) < 2:
      return False
    else:
      for i in range(len(l)):
        for j in range(len(l)):
          if i != j and l[i] + l[j] == 0:
            return True
      return False
    # END PROBLEM 1


def pairs_sum_to_n(l, n):
    """
    pairs_sum_to_n takes a list of integers as an input and a target
    integer n as an input.
    it returns True if there are two distinct elements in the list that
    sum to n, and False otherwise.
    >>> pairs_sum_to_n([1, 3, 5, 7], 10)
    True
    >>> pairs_sum_to_n([1, 3, 5, 7], 11)
    False
    >>> pairs_sum_to_n([1, 3, 5, 7], 9)
    True
    >>> pairs_sum_to_n([1, 3, 5, 7], 8)
    False
    >>> pairs_sum_to_n([1, 3, 5, 7], 6)
    False
    >>> pairs_sum_to_n([1, 3, 5, 7], 7)
    True
    >>> pairs_sum_to_n([1], 1)
    True
    >>> pairs_sum_to_n([1, 3, 5, 7], 100)
    False
    
	Do not include these tokens in the code: # 1 .
	"""
    # BEGIN PROBLEM 2
    if len(l) < 2:
      return False
    else:
      for i in range(len(l)):
        for j in range(len(l)):
          if i != j and l[i] + l[j] == n:
            return True
      return False
    # END PROBLEM 2


def linear_search(l, e):