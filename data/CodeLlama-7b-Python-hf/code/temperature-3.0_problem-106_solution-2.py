def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    factorial = lambda n: 1 if n <= 1 else n * factorial(n - 1)
    return [factorial(i) if i % 2 == 0 else (1 if i == 1 else sum(range(i + 1))) for i in range(n)]


