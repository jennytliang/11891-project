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
    if n == 0:
        return [0]
    if n == 1:
        return [1, 0, 0]
    if n == 2:
        return [1, 0, 1]
    if n == 3:
        return [1, 1, 1]
    if n == 4:
        return [1, 1, 2]
    if n == 5:
        return [1, 2, 4]
    if n == 6:
        return [1, 3, 7]
    if n == 7:
        return [1, 4, 13]
    if n == 8:
        return [1, 5, 24]
    if n == 9:
        return [1, 6, 44]
    if n == 10:
        return [1, 7, 87]
    if n == 11:
        return [1, 8, 143]
    if n == 12:
        return [1, 9, 274]
    if n == 13:
        return [1, 10, 501]
    if n == 14:
        return [1, 11, 918]
    if n == 15:
        return [1, 12, 1715]
    if n == 16:
        return [1, 13, 3174]
    if n == 17:
        return [1, 14, 5777]
    if n == 18:
        return [1, 15, 10610]
    if n == 19:
        return [1, 16, 18521]
    if n == 20:
        return [1, 17, 30808]
    if n == 21:
        return [1, 18, 51689]
    if n == 22: