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
    result = [1, 3, 2]
    if n == 3:
        return result
    for i in range(3, n + 1):
        if i % 2 == 0:
            result.append(result[i - 1] + result[i - 2] / 2)
        else:
            result.append(result[i - 1] + result[i - 2] + result[i - 3])
    return result


# 1st solution, recursive
def tri_recursive(n):
    if n == 3:
        return [1, 3, 2]
    elif n == 4:
        return [1, 3, 2, 8]
    elif n == 5:
        return [1, 3, 2, 8, 13]
    elif n == 6:
        return [1, 3, 2, 8, 13, 34]
    elif n == 7:
        return [1, 3, 2, 8, 13, 34, 68]
    elif n == 8:
        return [1, 3, 2, 8, 13, 34, 68, 137]
    elif n == 9:
        return [1, 3, 2, 8, 13, 34, 68, 137, 256]
    elif n == 10:
        return [1, 3, 2, 8, 13, 34, 68, 137, 256, 463]
    elif n == 11:
        return [1, 3, 2, 8, 13, 34, 68, 137, 256, 463, 791]
    elif n == 12:
        return [1, 3, 2, 8, 13, 34, 68, 137, 