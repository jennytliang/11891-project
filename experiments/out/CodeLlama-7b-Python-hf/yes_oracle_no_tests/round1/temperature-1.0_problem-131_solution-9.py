def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd , prod
	Do not include these tokens in the code: product
	"""
    pass


# tests
if __name__ == '__main__':
    # Store result in a variable.
    # Use a single statement with no intermediate variables.
    # Do not modify the return statement of this function.
    # Do not use magic numbers in your code.
    # Do not use any built-in Python functions.
    # You can create your own.
    # https://docs.python.org/3/library/functions.html
    # https://docs.python.org/3/library/stdtypes.html
    # You can use any of the following Python data types:
    # int, float, str, bool, list, tuple, dict, set, object
    # You can only use the following Python operations:
    # +, -,*,/,%,==,!=,>,>=,<,<=,and,or,not,in,is,+=,*=,+=,/=
    # You can only use the following Python classes:
    # int, float, str, bool, list, tuple, dict, set, object
    # You can only use the following Python functions:
    # abs, all, any, chr, dict, divmod, enumerate, filter, float, hex, id, int, iter, len, list, map, max, min, next, oct, ord, pow, range, repr, reversed, round, set, sorted, sum, tuple, zip,
    # You can only use the following Python modules:
    import math
    import sys
    import string
    import random
    import datetime
    import time
    import collections
    import statistics
    import operator

    # write your code below
    assert digits(1) == 1
    assert digits(2) == 0
    assert digits(10) == 0
    assert digits(11) == 1
    assert digits(235) == 15
    assert digits(12345) == 30
    assert digits(987654) == 0
    assert digits(10101) == 10000
    assert digits(11111) == 0
    assert digits(12