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
    
	Do not include these tokens in the code: def tri ( n ):
	"""
    a = 1
    b = 3
    c = 2
    result = [a, b, c]
    for i in range(1, n+1):
        if i % 2 == 0:
            result.append(result[i] + result[i] / 2)
        else:
            result.append(result[i-1] + result[i] + result[i+1])
    return result

def tri2(n):
    a = 1
    b = 3
    c = 2
    result = [a, b, c]
    for i in range(3, n+1):
        result.append(result[i-1] + result[i] + result[i+1])
    return result

print(tri(3))
print(tri2(3))