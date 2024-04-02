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
        if n == 1:
            return [1]
        elif n == 2:
            return [1, 3]
        elif n == 3:
            return [1, 3, 2]
        else:
            a = tri(2)
            b = tri(1)
            c = tri(3)
            d = []
            for i in range(n):
                if i % 2 == 0:
                    d.append(int(i / 2) + 1)
                else:
                    d.append(a[i - 1] + b[i - 2] + c[i - 3])
            return d
    return tri(n)


# 1
def tri(n):
    a = [1, 3]
    if n < 3:
        return a[:n]
    else:
        for i in range(2, n):
            a.append(a[i - 1] + a[i - 2] + a[i - 3])
    return a

# 2
def tri(n):
    a = [1, 3]
    if n < 3:
        return a[:n]
    else:
        for i in range(2, n):
            a.append(a[i - 1] + a[i - 2] + a[i - 3])
    return a

# 3
def tri(n):
    a = [1, 3]
    if n < 3:
        return a[:n]
    else:
        for i in range(2, n):
            a.append(a[i - 1] + a[i - 2] + a[i - 3])
    return a

# 4
def tri(n):
    a = [1, 3]
    if n < 3:
        return a[:n]
    else:
        for i in range(2, n):
            a.append(a[i - 1] + a[i - 2] + a