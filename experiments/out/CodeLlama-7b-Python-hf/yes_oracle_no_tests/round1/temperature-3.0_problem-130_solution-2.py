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
    
	Include these tokens in the code: if n ==
	"""
    if n == 1:
        return [1]
    if n == 2:
        return [1, 3]
    if n == 3:
        return [1, 3, 2]
    if n > 3:
        x = [1, 3, 2]
        for i in range(3, n):
            x.append(x[i] + x[i - 1] + x[i - 2])
        return x


def tri_f(n):
    """Using Fibonacci numbers"""
    if n == 1:
        return [1]
    if n == 2:
        return [1, 3]
    if n == 3:
        return [1, 3, 2]
    if n > 3:
        x = [1, 3, 2]
        for i in range(3, n):
            x.append(x[i] + x[i - 1] + x[i - 2])
        return x


def tri_r(n):
    """Using recursion"""
    if n == 1:
        return [1]
    if n == 2:
        return [1, 3]
    if n == 3:
        return [1, 3, 2]
    if n > 3:
        x = tri_r(n - 1)
        x.append(x[-1] + x[-2] + x[-3])
        return x
