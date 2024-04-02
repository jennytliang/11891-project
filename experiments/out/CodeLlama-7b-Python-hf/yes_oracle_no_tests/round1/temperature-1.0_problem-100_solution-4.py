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
    ans = list()
    num = n 
    
    # your code to create a list ans of answer
    # ans = []
    
    while num >= 1:
        even = 0
        if num % 2 == 0:
            even = num
        odd = 0
        if (num - 1) % 2 != 0:
            odd = num
        num = min(odd, even)
        ans.append(num)
    return ans[::-1]
    
assert make_a_pile(8) == [8, 7, 5, 3, 1]
assert make_a_pile(4) == [4, 5, 3, 1]
assert make_a_pile(6) == [6, 5, 3, 1]
