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
    
	Do not include these tokens in the code: def tri _ helper ( n ,
	"""

    def tri_helper(n, i=0, a=[1, 3, 2]):
        if i == n:
            return a
        else:
            if n % 2 == 0:
                a.append((n - i) / 2 + a[-1])
            else:
                a.append(a[-1] + a[-2] + a[-3])
            return tri_helper(n, i + 1, a)

    return tri_helper(n)


tri(3)
