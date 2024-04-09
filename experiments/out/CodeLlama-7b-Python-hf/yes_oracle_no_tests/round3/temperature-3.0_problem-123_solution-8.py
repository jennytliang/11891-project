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
    
	Include these tokens in the code: ans ,
	Do not include these tokens in the code: # TODO : Write your solution here
	"""
    pass

if __name__ == '__main__':
    # Test Case 1
    n = 5
    expected = [1, 5]
    result = get_odd_collatz(n)
    if expected == result:
        print("Test 1 for get_odd_collatz passes")
    else:
        print("Test 1 for get_odd_collatz fails. Expected:", expected," Got:", result)
    
    # Test Case 2
    n = 100
    expected = [1, 100]
    result = get_odd_collatz(n)
    if expected == result:
        print("Test 2 for get_odd_collatz passes")
    else:
        print("Test 2 for get_odd_collatz fails. Expected:", expected," Got:", result)
