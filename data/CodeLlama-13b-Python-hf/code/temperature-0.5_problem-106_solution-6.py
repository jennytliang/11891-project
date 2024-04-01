def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    return [1 if i % 2 == 0 else sum(range(1, i + 1)) for i in range(1, n + 1)]


def test_function():
    assert f(5) == [1, 2, 6, 24, 15]
    assert f(1) == [1]
    assert f(2) == [1, 3]
    assert f(8) == [1, 2, 6, 24, 15, 105, 945, 10395]
