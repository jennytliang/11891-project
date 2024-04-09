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
    
	Do not include these tokens in the code: # pass # remove the
	"""
    import math
    
    def isPrime(n):
        if n > 1:
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            else:
                for current in range(3, int(math.sqrt(n) + 1), 2):
                    if n % current == 0:
                        return False
                return True
        else:
            return False
    
    lst = [x for x in lst if x != 0]
    if lst == []:
        return 0
    largestPrime = max(lst)
    largestPrime = max([x for x in lst if isPrime(x)])
    largestPrimeDigits = [int(x) for x in str(largestPrime)]
    return sum(largestPrimeDigits)



lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3]
print(skjkasdkd(lst))

lst = [1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1]
print(skjkasdkd(lst))

lst = [1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3]
print(skjkasdkd(lst))

lst = [0,724,32,71,99,32,6,0,5,91,83,0,5,6]
print(skjkasdkd(lst))

lst = [0,81,12,3,1,21]
print(skjkasdkd(lst))

lst = [0,8,1,2,1,7]
print(skjkasdk