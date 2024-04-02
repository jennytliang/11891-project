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
    return [1 if i == 1 else sum(range(i)) if i % 2 else math.factorial(i) for i in range(1, n+1)]
    
    
def f_lambda(n):
    """ Same as f but using lambda.
    """
    # YOUR CODE HERE
    return list(map(lambda i: 1 if i == 1 else sum(range(i)) if i % 2 else math.factorial(i), range(1, n+1)))


print(f(5))
print(f_lambda(5))