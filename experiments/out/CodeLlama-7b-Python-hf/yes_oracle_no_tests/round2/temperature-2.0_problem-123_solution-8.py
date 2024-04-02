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
    
	Include these tokens in the code: = x
	"""

    ans, x = [], n
    while x != 1:
        if x % 2 == 1:
            ans.apend(x)
        x = x // 2 if x % 2 == 0 else 3 * x + 1
    return ans

print(get_odd_collatz(5))
print(get_odd_collatz(15))
print(get_odd_collatz(25))
print(get_odd_collatz(35))
print(get_odd_collatz(55))
print(get_odd_collatz(75))
print(get_odd_collatz(95))
print(get_odd_collatz(115))
print(get_odd_collatz(135))
print(get_odd_collatz(155))
print(get_odd_collatz(175))
print(get_odd_collatz(195))
print(get_odd_collatz(215))
print(get_odd_collatz(235))
print(get_odd_collatz(255))
print(get_odd_collatz(275))
print(get_odd_collatz(295))
print(get_odd_collatz(315))
print(get_odd_collatz(335))
print(get_odd_collatz(355))
print(get_odd_collatz(375))
print(get_odd_collatz(395))
print(get_odd_collatz(415))
print(get_odd_collatz(435))
print(get_odd_collatz(455))
print(get_odd_collatz(475))
print(get_odd_collatz(495))
print(get_odd_collatz(515))
print(get_odd_collatz(535))
print(get_odd_collatz(555))
print(get_odd_collatz(575))
print(get_odd_collatz(595))
print(get_odd_collatz(615))
print(get_odd_collatz(635