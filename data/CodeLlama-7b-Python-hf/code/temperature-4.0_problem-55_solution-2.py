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

      f_i, f_n = f_i_m2, f_i_m1  # swap f_i with the value from previous step (the old one in the old F(i))  (and rename f_n f_i) and set the new on to f_i (old one in current step). The new one, we will set it later)

      f_i_m1 += f_i_m2

      f_i_m2 = f_n

      a_i = next((n / x for x in count(1) if n % x == 0 and x < fib(f_i)))


