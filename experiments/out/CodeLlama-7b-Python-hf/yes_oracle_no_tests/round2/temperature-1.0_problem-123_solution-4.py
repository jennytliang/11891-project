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
    
	Include these tokens in the code: ans , x = [], n
	"""

    ###############
    # The CODE below


	# This is a list that I want to fill with the odd numbers in the collatz sequence.
    # This list is called 'ans'.
    ans = []
    
    # I want to iterate through the sequence until I have all odd Collatz numbers.
    while len(ans) != n:
        # As long as 'x' is an even number larger than 2, double it. I set x to 2, because that's an even number.
        # If x is set too large, it will cause a while loop. By setting x to 2, I can prevent that. 
        if x % 2 == 0 and x > 2:
            x *= 2
        # If x is an odd number larger than 3, then 3 times it. I set x to 3, for the same reason I set it up for evens.
        elif x % 2 == 1 and x > 3:
            x *= 3
        # Now I need to add x to 'ans'.
        elif x % 2 == 0 and x < 2:
            x = 3
        elif x % 2 == 1 and x < 3:
            x = 2
            ans.append(x)
        
    # Print the sequence here.
    return ans
