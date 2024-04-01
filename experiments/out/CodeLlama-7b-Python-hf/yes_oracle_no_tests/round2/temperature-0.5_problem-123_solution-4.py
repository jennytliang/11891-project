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
	Do not include these tokens in the code: = [ 1 ]
	"""


 
    if n == 1:
        return [1]
    elif n % 2 == 0:
        return get_odd_collatz(n / 2)
    else:
        return get_odd_collatz(3 * n + 1)
    
    # pass




def test_function(test_case):
    solution = get_odd_collatz(test_case[0])
    solution.sort()
    if solution == test_case[1]:
        print("Pass")
    else:
        print("Fail")


test_function([5, [1, 5]])
test_function([17, [1, 17, 16, 8, 4, 2, 1]])
test_function([33, [1, 33, 107, 53, 170, 85, 42, 21, 10, 5, 16, 8, 4, 2, 1]])
test_function([43, [1, 43, 124, 62, 31, 104, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]])
test_function([19, [1, 19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]])
test_function([47, [1, 47, 194, 97, 485, 242, 121, 60, 30, 15, 45, 23, 7, 21, 14, 28, 14, 28, 14, 28, 14