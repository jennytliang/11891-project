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
    
	Include these tokens in the code: 1
	Do not include these tokens in the code: 0
	"""


    ans, x = [], n
    
    while x != 1:
        i = x
        if i % 2 == 0:
            x = i // 2
        else:
            x = 3 * i + 1
        ans.append(i)
            
    return sorted([n] + ans)


def test_function(test_case):
    output = get_odd_collatz(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        return True
    else:
        return False


test_case_1 = [5, [1, 5]]
test_case_2 = [13, [1, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]]
test_case_3 = [1, [1]]

test1 = test_function(test_case_1)
test2 = test_function(test_case_2)
test3 = test_function(test_case_3)

print(test1, test2, test3)