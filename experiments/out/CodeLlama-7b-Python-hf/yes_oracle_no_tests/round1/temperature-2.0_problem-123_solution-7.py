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
    #code here
    x = []
    while n > 0:
        if n % 2 == 1:
            x.append(n)
        n = n//2 if n % 2 == 0 else 3*n + 1
    return sorted(x)


# Testing Code
print(get_odd_collatz(10))
print(get_odd_collatz(12))
print(get_odd_collatz(13))
print(get_odd_collatz(15))
print(get_odd_collatz(17))
print(get_odd_collatz(19))
print(get_odd_collatz(21))
print(get_odd_collatz(23))
print(get_odd_collatz(25))
print(get_odd_collatz(27))
print(get_odd_collatz(29))
print(get_odd_collatz(31))
print(get_odd_collatz(33))
print(get_odd_collatz(35))
print(get_odd_collatz(37))
print(get_odd_collatz(39))
print(get_odd_collatz(41))
print(get_odd_collatz(43))
print(get_odd_collatz(45))
print(get_odd_collatz(47))
print(get_odd_collatz(49))
print(get_odd_collatz(51))
print(get_odd_collatz(53))
print(get_odd_collatz(55))
print(get_odd_collatz(57))
print(get_odd_collatz(59))
print(get_odd_collatz(61))
print(get_odd_collatz(63))
print(get_odd_collatz(65))
print(get_odd_collatz(67))
print(get_odd_collatz(69))
print(get_odd_collatz(71))
print(get_odd_collatz(7