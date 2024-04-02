def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    
	Include these tokens in the code: def judge ( x ):
	Do not include these tokens in the code: result = [] for i
	"""
    return [i for i in x if not any(int(j) % 2 == 0 for j in str(i))]


#  def unique_digits(x):
#      """Given a list of positive integers x. return a sorted list of all 
#      elements that hasn't any even digit.

#      Note: Returned list should be sorted in increasing order.
    
#      For example:
#      >>> unique_digits([15, 33, 1422, 1])
#      [1, 15, 33]
#      >>> unique_digits([152, 323, 1422, 10])
#      []
    
#       Include these tokens in the code: def judge ( x ):
#       Do not include these tokens in the code: result = [] for i
#      """
#      result = []
#      for i in x:
#          judge = True
#          for j in str(i):
#              if int(j) % 2 == 0:
#                  judge = False
#              else:
#                  judge = True
#          if judge:
#              result.append(i)
#      return sorted(result)
