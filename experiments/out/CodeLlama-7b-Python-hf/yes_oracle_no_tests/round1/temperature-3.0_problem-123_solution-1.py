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
    # TODO: Write your solution here
    # 1. check if n is positive integer
    if type(n) != int or n <= 0:
        raise ValueError
    
    # 2. check if n is odd
    if n % 2 == 1:
        # 3. add n to ans
        x.append(n)
    
    # 4. if n is odd, call get_odd_collatz(n//2)
    if n % 2 == 1:
        get_odd_collatz(n//2)
    
    # 5. if n is even, return ans
    return x


if __name__ == "__main__":
    import doctest
    doctest.testmod()
