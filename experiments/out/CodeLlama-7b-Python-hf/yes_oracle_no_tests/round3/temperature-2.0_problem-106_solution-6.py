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
    res = []
    for i in range(1, n+1):
        if i % 2 == 0:
            res.append(fact(i))
        else:
            res.append(sum(range(1,i+1)))
    return res

def fact(n):
    return 1 if n == 0 else n * fact(n-1)


def test_function(test_case):
    test_case = test_case[0]
    solution = test_case[1]
    output = f(test_case)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

test_function([[5, [1, 2, 6, 24, 15]]])
test_function([[10, [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]]])
test_function([[5, [1, 2, 6, 24, 15]]])
test_function([[10, [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]]])
test_function([[5, [1, 2, 6, 24, 15]]])
test_function([[10, [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]]])
test_function([[5, [1, 2, 6, 24, 15]]])
test_function([[10, [1, 2, 6, 24, 120, 720, 5040, 40320, 36288