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
    # YOUR CODE HERE
    a = []
    for i in range(1, n+1):
        if i % 2 == 0:
            a.append(f(i))
        else:
            a.append(sum(range(1, i+1)))
    return a



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
    # YOUR CODE HERE
    a = []
    for i in range(1, n+1):
        if i % 2 == 0:
            a.append(f(i))
        else:
            a.append(sum(range(1, i+1)))
    return a

# 1 2 6 24 15
# 1 3 6 24 15
# 1 3 6 36 15
# 1 3 6 36 15
# 1 3 6 36 15
# 1 3 6 36 15
# 1 3 6 36 15
# 1 3 6 36 15
# 1 3 6 36 15
# 1 3 6 36 15
# 1 3 6 36 15
# 1 3 6 36 15
# 1 3 6 36 15
# 1 3 6 36 15
# 1 3 6 3