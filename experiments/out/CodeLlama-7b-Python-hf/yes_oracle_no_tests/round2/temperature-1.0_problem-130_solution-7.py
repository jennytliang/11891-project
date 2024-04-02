def tri(n):
    """Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in 
    the last couple centuries. However, what people don't know is Tribonacci sequence.
    Tribonacci sequence is defined by the recurrence:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    For example:
    tri(2) = 1 + (2 / 2) = 2
    tri(4) = 3
    tri(3) = tri(2) + tri(1) + tri(4)
           = 2 + 3 + 3 = 8 
    You are given a non-negative integer number n, you have to a return a list of the 
    first n + 1 numbers of the Tribonacci sequence.
    Examples:
    tri(3) = [1, 3, 2, 8]
    
	Include these tokens in the code: 1
	Do not include these tokens in the code: 0
	"""

    if n == 0:
    # return [1]
    # return [0,1]
        return [1,1,1]
    elif n == 1:
        return [1,1,1,3]
    else:
        return [1,1,1] + tri(n-1)

print tri(10)


def is_power_of_two(n):
    """You are given a positive integer n. Determine whether it can be represented as an
    exponent of two.
    Examples:
    is_power_of_two(16) = True
    is_power_of_two(9) = False
    is_power_of_two(1024) = True
    is_power_of_two(3) = False
    is_power_of_two(0) = False
    is_power_of_two(1) = True
    is_power_of_two(5) = False
    
	Include these tokens in the code: 1
	Do not include these tokens in the code: 0
    """
    if n == 0:
        return False
    elif n == 1:
        return True
    elif n % 2 == 1:
        return False
    else:
        return is_power_of_two(n / 2)

print is_power_of_two(2)


def is_power_of_three(n):
    """You are given a positive integer n. Determine whether it can be represented as an
    exponent of three.
    Examples:
    is_power_of_three(27) = True
    is_power_of_three(9) = False
    is_power_of_three(1000) = False
    is_power_of_three(3) = True
    is_power_of_three(0) = False
    is_power_of_three(1) = True
    is_power_of_three(5) = False
    
	Include these tokens in the code: 1
	Do not include these tokens in the code: 0
    """
