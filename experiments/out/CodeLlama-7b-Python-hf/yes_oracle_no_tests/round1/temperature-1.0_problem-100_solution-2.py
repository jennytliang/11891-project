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
    num = []
    ans = []
    while n != 0:
        if n%2!=0:
            answer = n
        else:
            answer = n+1
        n = n-answer
        num.append(answer)

    n = len(num)
    for x in range(n):
        ans.append(sum(num[:x+1]))

    return ans


print(make_a_pile(3))