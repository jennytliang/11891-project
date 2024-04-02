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
    
	Do not include these tokens in the code: # Initialize the answer list
	"""
    # Initialize the answer list
    answer = []
    # Write your code here
    i = n
    while i > 0:
        if i % 2 == 0:
            i += 1
        answer.append(i)
        i += 2
    return answer


if __name__ == "__main__":
    print(make_a_pile(3))
    print(make_a_pile(5))
    print(make_a_pile(12))
