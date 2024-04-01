def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    f_i_m2 = 0  # F(i-2)
    f_i_m1 = 1  # F(i-1)
    f_i = 1  # F(0): this and next line are initial F(i)
    f_n = f_i - f_i  # we initialize f(i-1): f_(n) = - f_n (because of the way we count,
    # this value is not relevant anyway, but we put it in

    while f_i_m1 != f_i:

      f_i, f_n = f_n, f_i