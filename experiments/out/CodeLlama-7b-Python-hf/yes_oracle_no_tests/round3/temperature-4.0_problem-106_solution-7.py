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
    res = [0] * n
    for i in range(n):
        if i % 2 == 0:
            res[i] = 1
            for j in range(1, i + 1):
                res[i] *= j
        else:
            res[i] = 0
            for j in range(1, i + 1):
                res[i] += j
    return res


def test_f():
    assert f(5) == [1, 2, 6, 24, 15]
    assert f(3) == [1, 2, 3, 6, 15]
    assert f(1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
