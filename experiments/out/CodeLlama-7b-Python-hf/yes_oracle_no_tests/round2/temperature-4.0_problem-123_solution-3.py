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
    
	Include these tokens in the code: ans
	Do not include these tokens in the code: # The Coll atz conject ure is
	"""
    # 1. check input type
    if not isinstance(n, int):
        raise TypeError(f"n is {n} and must be an int")
    if n <= 0:
        raise ValueError(f"n is {n} and must be a positive integer")
    # 2. create answer list
    ans = []
    # 3. get odd collatz
    while n not in ans:
        ans.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    # 4. return answer list
    return ans


def get_even_collatz(n):
    """
    Given a positive integer n, return a sorted list that has the even numbers in collatz sequence.

    The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined
    as follows: start with any positive integer n. Then each term is obtained from the previous term as follows: if the previous term is even, the next term is one half of the previous term. If the previous term is odd, the next term is 3 times the previous term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.

    Note: 
        1. Collatz(1) is [1].
        2. returned list sorted in increasing order.

    For example:
    get_even_collatz(5) returns [8, 4] # The collatz sequence for 5 is [5, 16, 8, 4, 2, 1], so the even numbers are only 8, and 4.
    
	Include these tokens in the code: ans
	Do not include these tokens in the code: # The Coll atz conject ure is
	"""
    # 1. check input type
    if not isinstance(n, int):
        raise TypeError(f"n is {n} and must be an int")
    if n <= 0:
        raise ValueError(f"n is {n} and must be a positive integer")
    # 2. create answer list
   