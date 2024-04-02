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
    return None


def test_f():
    assert f(5) == [1, 2, 6, 24, 15]
    assert f(10) == [1, 2, 6, 24, 15, 120, 720, 5040, 40320, 362880]
    assert f(0) == [1]
    assert f(1) == [1, 1]
    assert f(2) == [1, 2, 2]
    assert f(3) == [1, 2, 6, 6]
    assert f(4) == [1, 2, 6, 24, 24]


if __name__ == '__main__':
    test_f()
