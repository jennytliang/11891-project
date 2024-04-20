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
    for i in range(1, n + 1):
        if i % 2 == 0:
            list.append(factorial(i))
        else:
            sum = 0
            for j in range(1, i + 1):
                sum += j
            list.append(sum)
    return list


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(f(5))