def skjkasdkd(lst):
    """You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.

    Examples:
    For lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3] the output should be 10
    For lst = [1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1] the output should be 25
    For lst = [1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3] the output should be 13
    For lst = [0,724,32,71,99,32,6,0,5,91,83,0,5,6] the output should be 11
    For lst = [0,81,12,3,1,21] the output should be 3
    For lst = [0,8,1,2,1,7] the output should be 7
    
	Include these tokens in the code: def is _ prime ( a ): return
	"""
    
    def is_prime(a):
        for i in range(2, a):
            if (a % i) == 0:
                return False
        return True
    
    def sum_of_digits(n):
        s = 0
        while n > 0:
            s += n % 10
            n = n // 10
        return s
    
    lst = sorted(lst)
    lst.reverse()
    lst2 = []
    for i in lst:
        if is_prime(i):
            lst2.append(i)
    lst2 = sorted(lst2)
    lst2.reverse()
    s = 0
    for i in lst2:
        s += sum_of_digits(i)
    return s


print(skjkasdkd([0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3]))
print(skjkasdkd([1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1]))
print(skjkasdkd([1, 3, 1, 32, 5107, 34, 83278, 109, 163, 23, 2323, 32, 30, 1, 9, 3]))
print(skjkasdkd([0, 724, 32, 71, 99, 32, 6, 0, 5, 91, 83, 0, 5, 6]))
print(skjkasdkd([0, 81, 12, 3, 1, 21]))
print(