def correct_bracketing(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    
	Include these tokens in the code: c nt =
	"""
    # YOUR CODE HERE

    cnt = 0 # The number of opening brackets
    for char in brackets:
      if char == '<':
        cnt += 1
      elif char == '>':
        cnt -= 1
      if cnt < 0:
        return False
    ###
    return cnt == 0
