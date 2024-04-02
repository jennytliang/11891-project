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
    i = 1
    res = []
    while i != n:
        while i > 0:
            i += f(i)
            if i % 2 == 0:
                res.append(int(i))
            i -= 1
    return res
if __name__ == '__main__':
    print(f(5))