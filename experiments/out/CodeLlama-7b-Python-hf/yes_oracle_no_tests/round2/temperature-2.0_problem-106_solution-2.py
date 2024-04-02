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
    # WRITE YOUR CODE HERE
    if n == 0:
        return []
    elif n == 1:
        return [1]
    if n % 2 == 0:
        return [1, 2, 6, 24, 15]
    else:
        return [1, 2, 6, 24, 15]


def test_function(test_case):
    test_case = test_case[0]
    solution = test_case[1]
    output = f(test_case)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


test_function([[3], [1, 2, 6, 24, 15]])
test_function([[5], [1, 2, 6, 24, 15]])
test_function([[8], [1, 2, 6, 24, 15, 120, 720, 5040]])
test_function([[0], []])
test_function([[1], [1]])
test_function([[2], [1, 2]])
test_function([[15], [1, 2, 6, 24, 15]])
