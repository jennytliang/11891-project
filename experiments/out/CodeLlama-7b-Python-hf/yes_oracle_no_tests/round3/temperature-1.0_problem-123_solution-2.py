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
	"""
    # pass
    ans = []
    while n > 1:
        if n % 2 != 0:
            ans.append(n)
        n = n * 3 + 1
    return ans


def test_function(test_case):
    answer = get_odd_collatz(test_case[0])
    if answer == test_case[1]:
        print("Pass")
    else:
        print("Fail")


test_case_1 = [13, [1, 13]]
test_function(test_case_1)

test_case_2 = [5, [1, 5]]
test_function(test_case_2)

test_case_3 = [1, [1]]
test_function(test_case_3)

test_case_4 = [3, [3]]
test_function(test_case_4)

test_case_5 = [17, [1, 5, 17]]
test_function(test_case_5)

test_case_6 = [100, [1, 5, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1, 100]]
test_function(test_case_6)
