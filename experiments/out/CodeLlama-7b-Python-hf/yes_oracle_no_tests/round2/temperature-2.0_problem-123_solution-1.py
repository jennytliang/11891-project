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
    
	Include these tokens in the code: ,
	Do not include these tokens in the code: = []
	"""

   pass


result = get_odd_collatz(5)
print(result)

result = get_odd_collatz(15)
print(result)

result = get_odd_collatz(100000)
print(result)


# 1.
# get_odd_collatz(5) returns [1, 5] # The collatz sequence for 5 is [5, 16, 8, 4, 2, 1], so the odd numbers are only 1, and 5.

# 2.
# get_odd_collatz(15) returns [1, 15, 5, 13] # The collatz sequence for 15 is [15, 40, 20, 10, 5, 16, 8, 4, 2, 1], so the odd numbers are 1, 15, 5, and 13.

# 3.
# get_odd_collatz(100000) returns [1, 100000, 50000, 166666, 83333, 41666, 20833, 10416, 5208, 2604, 1302, 651, 325, 162, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1] # This sequence is very long, so you will need to find a way to simplify your code so that it is not too slow.

