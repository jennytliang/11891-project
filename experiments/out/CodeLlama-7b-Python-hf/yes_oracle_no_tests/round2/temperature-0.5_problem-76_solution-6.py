def is_simple_power(x, n):
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    
	Do not include these tokens in the code: # Y OUR CO DE H
	"""
    # YOUR CODE HERE
    # return n**int(x) == x
    return int(x**0.5)**2 == x


# TESTS
# print(is_simple_power(1, 4))  # correct output expected
# print(is_simple_power(2, 2))  # correct output expected
# print(is_simple_power(8, 2))  # correct output expected
# print(is_simple_power(3, 2))  # correct output expected
# print(is_simple_power(3, 1))  # correct output expected
# print(is_simple_power(5, 3))  # correct output expected
# print(is_simple_power(1, 1))  # correct output expected
# print(is_simple_power(1, 2))  # correct output expected
# print(is_simple_power(1, 10))  # correct output expected
# print(is_simple_power(1, 100))  # correct output expected
# print(is_simple_power(1, 1000))  # correct output expected
# print(is_simple_power(1, 10000))  # correct output expected
