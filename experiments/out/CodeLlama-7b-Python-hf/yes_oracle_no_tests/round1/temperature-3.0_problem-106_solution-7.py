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
    def fact(n):
        if n == 0:
            return 1
        else:
            return n * fact(n - 1)
    ans = []
    for i in range(n):
        if i % 2 == 0:
            ans.append(fact(i))
        else:
            ans.append(sum(range(i + 1)))
    return ans


def test_function(test_case):
    test_case = test_case[0]
    solution = test_case[1]
    output = f(test_case)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


test_function([[3, [1, 2, 6]]])
test_function([[5, [1, 2, 6, 24, 15]]])
test_function([[7, [1, 2, 6, 24, 15, 120, 720]]])
test_function([[10, [1, 2, 6, 24, 15, 120, 720, 5040, 40320, 362880]]])
