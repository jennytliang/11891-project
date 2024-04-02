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
	Do not include these tokens in the code: = []
	"""

  
    if n % 2 == 0:
        return [n]
    else:
        return [n] + get_odd_collatz(3 * n + 1)


def test_function(test_case):
    answer = get_odd_collatz(test_case[0])
    if answer == test_case[1]:
        print("Pass!")
    else:
        print("Fail!")


# test 1
test_case = [13, [1, 13, 5, 17, 19, 65, 165, 465, 665, 3325, 8625, 47625, 1395325]]
test_function(test_case)

# test 2
test_case = [1, [1]]
test_function(test_case)

# test 3
test_case = [14, [14, 40, 20, 10, 5, 16, 8, 4, 2, 1]]
test_function(test_case)

# test 4
test_case = [2, []]
test_function(test_case)

# test 5
test_case = [3, [3, 10, 5, 16, 8, 4, 2, 1]]
test_function(test_case)