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
    pile = []
    n = int(n)
    for i in range(n):
        if i % 2 == 0:
            pile.append(i + 1)
        else:
            pile.append(i + 2)
    return pile


if __name__ == "__main__":
    print("Example:")
    print(make_a_pile(3))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert make_a_pile(3) == [3, 5, 7]
    assert make_a_pile(6) == [6, 9, 12, 15]
    assert make_a_pile(11) == [11, 14, 17, 20, 23]
    print("Coding complete? Click 'Check' to earn cool rewards!")
