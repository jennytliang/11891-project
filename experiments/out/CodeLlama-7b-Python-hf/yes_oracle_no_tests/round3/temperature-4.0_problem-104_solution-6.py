def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    
	Include these tokens in the code: ch
	Do not include these tokens in the code: i
	"""


    def judge(x):
      ch = []
      for i in str(x):
        if int(i) % 2 == 1:
          ch.append(i)
      res = int(''.join(ch))
      return res

    return sorted(list(set([judge(i) for i in x])))





































