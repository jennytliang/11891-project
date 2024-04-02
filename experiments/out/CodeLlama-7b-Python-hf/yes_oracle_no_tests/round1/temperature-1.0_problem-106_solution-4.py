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

    # def even(n):
    #     if n % 2 == 0:
    #         return True
    #
    #     return False

    lis = []
    for i in range(1, n):
        if i % 2:
            lis.append(sum(range(1, i+1)))
        if i % 2 == 0:
            lis.append(factorial(i))
        # breakpoint()
    return lis


def factorial(n):
    if n == 0:
        return 1
    val = 1
    for i in range(1, n+1):
        val *= i
    return val

    #
### TEST

def test_function():
    # These 'asserts' using only for self-checking and not necessary for auto-testing
    assert f(4) == [1, 2, 6, 24]
    assert f(6) == [1, 2, 6, 24, 120, 720]


if __name__ == '__main__':
    test_function()
