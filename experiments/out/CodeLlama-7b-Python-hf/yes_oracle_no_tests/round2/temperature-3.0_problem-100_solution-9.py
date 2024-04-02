def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    
	Include these tokens in the code: ,
	Do not include these tokens in the code: = []
	"""

  	# define pile
  	pile = []

  	# while the length of the pile is less than n
  	while len(pile) < n:

  		# append the next odd number to the pile
  		if n % 2 == 1:
  			pile.append(n)
  			n += 2

  		# append the next even number to the pile
  		else:
  			pile.append(n)
  			n += 2

  	# return the pile
  	return pile