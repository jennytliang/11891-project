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
    def tri(n):
        if n == 0:
            return [1]
        elif n == 1:
            return [1, 3]
        elif n == 2:
            return [1, 3, 2]
        elif n == 3:
            return [1, 3, 2, 8]
        else:
            x = tri(n - 3)
            x.append(x[len(x) - 1] + x[len(x) - 2] + x[len(x) - 3])
            return x
    return tri(n)
print(tri(3))
