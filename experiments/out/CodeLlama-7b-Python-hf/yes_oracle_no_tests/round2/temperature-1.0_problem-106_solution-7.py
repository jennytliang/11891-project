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
    list = []
    i = 1
    for _ in range(1, n + 1):
        if i % 2 == 0:
            list.append(functools.reduce(operator.mul, range(1, int(i / 2) + 1), 1) * functools.reduce(operator.mul, range(int(i / 2 + 1), i + 1), 1))
        else:
            list.append(sum(list(range(1, i + 1))))
        i=i+1
    return list

import functools
import operator
