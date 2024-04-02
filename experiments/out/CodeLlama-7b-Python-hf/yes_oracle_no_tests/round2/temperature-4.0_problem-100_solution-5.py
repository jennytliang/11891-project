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

  
    if n == 1:
        return 1
    elif n % 2 == 0:
        return [n] + make_a_pile(n-1)
    else:
        return [n] + make_a_pile(n-2)


# print(make_a_pile(1))
# print(make_a_pile(3))
# print(make_a_pile(2))
# print(make_a_pile(4))
# print(make_a_pile(5))
# print(make_a_pile(6))
# print(make_a_pile(7))
# print(make_a_pile(8))
# print(make_a_pile(9))
# print(make_a_pile(10))
# print(make_a_pile(11))
# print(make_a_pile(12))
# print(make_a_pile(13))
# print(make_a_pile(14))
# print(make_a_pile(15))
# print(make_a_pile(16))
# print(make_a_pile(17))
# print(make_a_pile(18))
# print(make_a_pile(19))
# print(make_a_pile(20))
# print(make_a_pile(21))
# print(make_a_pile(22))
# print(make_a_pile(23))
# print(make_a_pile(24))
# print(make_a_pile(25))
# print(make_a_pile(26))
# print(make_a_pile(27))
# print(make_a_pile(28))
# print(make_a_pile(29))
# print(make_a_pile(30))
# print(make_a_pile(31))
# print(make_a_p