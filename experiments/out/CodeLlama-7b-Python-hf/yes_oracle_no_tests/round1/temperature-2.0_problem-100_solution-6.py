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
    
	Include these tokens in the code: ans , num = [], n
	"""
    # Initialize the answer list
    ans = []
    # Initialize the number of stones in the current level
    num = n
    # Add the number of stones in the first level
    ans.append(num)
    # While there are still some levels
    while num > 0:
        # If the number of stones in the current level is odd
        if num % 2 == 1:
            # Add one stone to the next level
            num += 2
        # Otherwise
        else:
            # Add two stones to the next level
            num += 4
        # Add the number of stones in the next level
        ans.append(num)
    # Return the number of stones in each level
    return ans


# Pybites solution
def make_a_pile1(n):
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
    
	Include these tokens in the code: ans , num = [], n
	"""
    # Initialize the answer list
    ans = []
    # Add the number of stones in the first level
    ans.append(n)
    # While there are still some levels
    while n > 1:
        # If the number of stones in the current level is odd
        if n % 2 == 1:
            # Add one stone to the next level
            n += 1
        # Otherwise
        else:
            # Add two stones to the next level
            n += 2
        # Add the number of stones in the next level
        ans.append(n)
    # Return the number of stones in each level
    return ans
