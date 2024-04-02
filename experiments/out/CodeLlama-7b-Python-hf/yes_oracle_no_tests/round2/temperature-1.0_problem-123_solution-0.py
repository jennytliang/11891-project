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
	Do not include these tokens in the code: # We want to check if this
	"""
    pass


def get_collatz(n):
    """
    Given a positive integer n, return a sorted list that has the numbers in collatz sequence.

    The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined
    as follows: start with any positive integer n. Then each term is obtained from the 
    previous term as follows: if the previous term is even, the next term is one half of 
    the previous term. If the previous term is odd, the next term is 3 times the previous
    term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.

	Input: 	n (int)
	Output: A list of intergers from 1 to n in the Collatz sequence sorted in 
	increasing order.
	For example:   get_collatz(5) returns [1, 1, 5] 
	               (Integers 1, 2, and 5 in the Colatz sequence).

    Note: 
        1. Collatz(1) is [1].
        2. returned list sorted in increasing order.

	Include these tokens in the code: ans
	Do not include these tokens in the code: # We want to check if this
	"""
    pass








"""
Test your code with this
Do not modify this code
"""
import sys
import functools


@functools.total_ordering
class Test:
    def __init__(self, func, inp, out):
        self.func = func
        self.inp = inp
        self.out = out

    def __eq__(self, other):
        try:
            result = \
                self.func(self.inp) == other.func(other.inp) and \
                self.out == other.out
            return result
        except Exception as ex:
            print("Test Error:" + ex)
            return False

    def __le__(self, other):
        return self.out <= other.out


def test_runner(tests):
    for test in