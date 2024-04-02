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
    result = []
    if n == 1:
        result.append(1)
    elif n == 2:
        result.append(1)
        result.append(3)
    elif n == 3:
        result.append(1)
        result.append(3)
        result.append(2)
    else:
        result.append(1)
        result.append(3)
        result.append(2)
        for i in range(4, n + 1):
            if i % 2 == 0:
                result.append(result[i - 1] + result[i - 2] + result[i - 3] / 2)
            else:
                result.append(result[i - 1] + result[i - 2] + result[i - 3] + result[i - 4])
    return result


print(tri(3))
print(tri(10))
print(tri(15))
print(tri(20))
print(tri(25))
print(tri(30))
print(tri(35))
print(tri(40))
print(tri(45))
print(tri(50))
print(tri(55))
print(tri(60))
print(tri(65))
print(tri(70))
print(tri(75))
print(tri(80))
print(tri(85))
print(tri(90))
print(tri(95))
print(tri(100))
print(tri(105))
print(tri(110))
print(tri(115))
print(tri(120))
print(tri(125))
print(tri(130))
print(tri(135))
print(tri(140))
print(tri(145))
print(tri(150))
print(tri(155))
print(tri(160))
print(tri(165))
print(tri(170))
print(tri(