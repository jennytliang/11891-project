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
    
	Include these tokens in the code:  ans , x = [], n
	"""

    ans = [1]
    x = n
    while x != 1:
        if x % 2 == 0:
            x = x//2
        else:
            x = 3*x + 1
        if x not in ans:
            ans.append(x)
    return ans

def main():
    print("Example:")
    print(get_odd_collatz(5))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert get_odd_collatz(5) == [1, 5]
    assert get_odd_collatz(14) == [1, 14, 12, 6, 3, 10, 5, 16, 8, 4, 2, 1]
    assert get_odd_collatz(100) == [1, 100, 50, 125, 62, 31, 94, 47, 188, 94, 47, 236, 118, 59, 177, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    assert get_odd_collatz(1) == [1]
    assert get_odd_collatz(2) == [1, 2]
    assert get_odd_collatz(3) == [1, 3]
    print("Coding complete? Click 'Check' to earn cool rewards!")
