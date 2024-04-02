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

  
    # Write your code here

    if n % 2 == 0:
        n = n + 1
    pile = []
    for i in range(n):
        pile.append(n)
        if n % 2 == 0:
            n = n + 2
        else:
            n = n + 1
    return pile


