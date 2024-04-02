def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    
	Include these tokens in the code: if n ==
	"""
    return [None for i in range(n)]



def test_function(test_case):
    output = f(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution) and output.count(1) == solution.count(1) and output.count(2) == solution.count(2) and output.count(6) == solution.count(6) and output.count(24) == solution.count(24) and output.count(120) == solution.count(120):
        print("Pass")
    else:
        print("Fail")

test_function([5, [1, 2, 6, 24, 120]])
test_function([6, [1, 2, 6, 24, 120, 720]])
test_function([7, [1, 2, 6, 24, 120, 720, 5040]])
test_function([8, [1, 2, 6, 24, 120, 720, 5040, 40320]])
test_function([9, [1, 2, 6, 24, 120, 720, 5040, 40320, 362880]])
test_function([10, [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]])




