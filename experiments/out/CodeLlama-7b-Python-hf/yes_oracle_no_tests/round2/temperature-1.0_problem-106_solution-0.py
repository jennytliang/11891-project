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
    n = int(n)
    result = []
    for i in range(1, n+1):
        if i % 2 == 0:
            result.append(factorial(i))
        else:
            result.append(sum(range(1, i+1)))
    return result

def factorial(n):
    """
    Implement the factorial function here
    """
    fact = 1
    while n >= 1:
        fact *= n
        n -= 1
    return fact


# ## Unit tests
# 
# Run the test file tests.py for this assignment.
# 
# Run the test file by typing the command:
# 
# `python tests.py`
# 
# in the terminal.

# ## Submission
# 
# Before you submit your solution to the grader, make sure to rename your file to "solution.py".
# 
# Then submit your solution as usual:
# 
# `submit solution.py`
# 
# NB: Do not leave the "solution.ipynb" notebooks in your folder, they won't be checked.

# ## Hints
# 
# * `range(6)` is `[0,1,2,3,4,5]`
# * `list(range(6))` is `[0,1,2,3,4,5]`
# * `list(range(1, 6))` is `[1,2,3,4,5]`
# * `list(range(1, 6, 2))` is `[1,3,5]`
# * `list(range(1, 6, 3))` is `[1,4]`
# * `list(range(6, 1, -2))` is `[6,4,2]`
# * `list(range(1, 6, 2))` is `[1,3,5]`
# * `list(range(1, 6, 3))` is `[1,4]`
# * `help(range)`
# * `help("range")`
# * `type(range(6))`
# * `type([