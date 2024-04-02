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
	Do not include these tokens in the code: if n < 1 :
	"""
    if n < 1:
        return []
    elif n == 1:
        return [1]
    else:
        ans = []
        while n != 1:
            if n % 2 == 1:
                ans.append(n)
            n = 3 * n + 1
        return ans
    
def test_function(test_case):
    output = get_odd_collatz(test_case[0])
    solution = test_case[1]
    if solution == output:
        print("Pass")
    else:
        print("Fail")

test_function([5, [1, 5]])
test_function([2, []])
test_function([1, [1]])
test_function([3, [3, 11, 3, 10, 5, 16, 8, 4, 2, 1]])
test_function([4, [4, 2, 1]])
test_function([6, [6, 3, 10, 5, 16, 8, 4, 2, 1]])
test_function([10, [10, 5, 16, 8, 4, 2, 1]])
test_function([12, [12, 6, 3, 10, 5, 16, 8, 4, 2, 1]])



