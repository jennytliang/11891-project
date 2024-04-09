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
    
    #%% Solution
    ans = []
    x = 1
    while x != 1:
        if x % 2 == 1:
            ans.append(x)
        x = 3 * x + 1 if x % 2 == 1 else x // 2
    return ans

#%% Test - Only run this test if you want to test your code
assert get_odd_collatz(5) == [1, 5]
assert get_odd_collatz(13) == [1, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
assert get_odd_collatz(21) == [1, 21, 64, 32, 16, 8, 4, 2, 1]
assert get_odd_collatz(45) == [1, 45, 90, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
