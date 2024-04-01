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

    # get the collatz sequence
    def collatz(n):
        if n % 2 == 0:
            return n / 2
        else:
            return 3 * n + 1

    # get the odd numbers in collatz sequence
    def get_odd(n):
        x = n
        ans = []
        while x != 1:
            if x % 2 == 1:
                ans.append(x)
                x = collatz(x)
            else:
                x = collatz(x)
        return ans

    # main
    return sorted(get_odd(n))


def test_function(test_case):
    output = get_odd_collatz(test_case[0])
    solution = test_case[1]
    if solution == output:
        print("Pass")
    else:
        print("Fail")

test_function([13, [1, 13, 34, 19, 5, 17, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]])
test_function([5, [1, 5, 16, 8, 4, 2, 1]])
test_function([12, [1, 12, 4, 2, 1]])
test_function([11, [1, 11, 32, 16, 8, 4, 2, 1]])
