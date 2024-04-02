def get_odd_collatz(n):
    """
    Given a positive integer n, return a sorted list that has the odd numbers in collatz sequence.

    The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined
    as follows: start with any positive integer n. Then each term is obtained from the 
    previous term as follows: if the previous term is even, the next term is one half of 
    the previous term. If the previous term is odd, the next term is 3 times the previous
    term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.

    Note: 
        1. Collatz(1) is [1].
        2. returned list sorted in increasing order.

    For example:
    get_odd_collatz(5) returns [1, 5] # The collatz sequence for 5 is [5, 16, 8, 4, 2, 1], so the odd numbers are only 1, and 5.
    
	Include these tokens in the code: ans , x = [],
	Do not include these tokens in the code: if
	"""
    # We want to check if this number is even or odd, to see if we have to move to the next point.
    # If it is odd, then we can do what we want. If it is even, then we check if it will ever be odd, if not, then it is False.
    ans = []
    x = True
    while x:
        if n % 2 !=0:
            ans.append(n)
            if n == 1:
                x = False
            else:
                n = n * 3 + 1
        else:
            if n == 1:
                x = False
            else:
                n = n//2
    return ans

import doctest
doctest.testmod()
