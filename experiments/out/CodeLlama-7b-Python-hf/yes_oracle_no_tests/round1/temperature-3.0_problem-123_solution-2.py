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
    ans = []
    x = n
    while x != 1:
        if x % 2 == 1:
            ans.append(x)
        x = 3 * x + 1 if x % 2 == 1 else x // 2
    ans.append(1)
    return ans


# Fibonacci
def get_fibonacci(n):
    """
    Given a positive integer n, return the nth number in the Fibonacci sequence.

    The Fibonacci numbers are the numbers in the following integer sequence,
    called the Fibonacci sequence, and characterized by the fact that every 
    number after the first two is the sum of the two preceding ones.

    Note: 
        1. n >= 0
        2. returned value is an integer.

    For example:
    get_fibonacci(7) returns 13
    
	Include these tokens in the code: ans , x = 0, y = 1, n
	"""
    ans = 0
    x = 0
    y = 1
    while n >= 1:
        ans = x + y
        x = y
        y = ans
        n -= 1
    return ans


# Test cases:
print(get_odd_collatz(5))
print(get_fibonacci(7))