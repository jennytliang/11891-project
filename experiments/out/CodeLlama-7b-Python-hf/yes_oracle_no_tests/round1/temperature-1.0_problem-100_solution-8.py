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
    ans = []
    num = []
    flag = n % 2
    for i in range(n):
        num.append(i + 1)
        if i < n:
            if flag == 1:
                ans.append(2 * num[i] + 1)
                flag = 0
            else:
                ans.append(2 * num[i] + 1)
                flag = 1
    return ans

print(make_a_pile(3))
print(make_a_pile(5))
print(make_a_pile(6))
print(make_a_pile(7))
print(make_a_pile(8))
