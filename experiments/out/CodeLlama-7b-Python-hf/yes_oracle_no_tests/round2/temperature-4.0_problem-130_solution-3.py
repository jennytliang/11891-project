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
        return [1, 1, 1]
    if n == 1:
        return [1, 1, 2]
    if n == 2:
        return [1, 1, 2, 4]
    if n > 2:
        lst = [1, 1, 2, 4]
        for i in range(3, n):
            lst.append(lst[i - 1] + lst[i - 2] + lst[i - 3])
        return lst


print(tri(3))
print(tri(4))
print(tri(5))
print(tri(6))
print(tri(7))
print(tri(8))
print(tri(9))
print(tri(10))
print(tri(11))
print(tri(12))
print(tri(13))
print(tri(14))
print(tri(15))
print(tri(16))
print(tri(17))
print(tri(18))
print(tri(19))
print(tri(20))
print(tri(21))
print(tri(22))
print(tri(23))
print(tri(24))
print(tri(25))
print(tri(26))
print(tri(27))
print(tri(28))
print(tri(29))
print(tri(30))
print(tri(31))
print(tri(32))
print(tri(33))
print(tri(34))
print(tri(35))
print(tri(36))
print(tri(37))
print(tri(38))
print(tri(39))
print(tri(40))
print(tri(41))
print(tri(42))
print(tri(43))
print(tri(44))
print(tri(45))
print(tri(46))
print(tri(47))
print(tri(48))
print(tri(49