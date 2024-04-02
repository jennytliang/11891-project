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
    largestPrime = 0
    for i in lst:
        if i > largestPrime:
            largestPrime = i
    if largestPrime == 0:
        return 0
    else:
        while largestPrime % 2 == 0:
            largestPrime = largestPrime / 2
        while largestPrime % 3 == 0:
            largestPrime = largestPrime / 3
        while largestPrime % 5 == 0:
            largestPrime = largestPrime / 5
        while largestPrime % 7 == 0:
            largestPrime = largestPrime / 7
        while largestPrime % 11 == 0:
            largestPrime = largestPrime / 11
        while largestPrime % 13 == 0:
            largestPrime = largestPrime / 13
        while largestPrime % 17 == 0:
            largestPrime = largestPrime / 17
        while largestPrime % 19 == 0:
            largestPrime = largestPrime / 19
        while largestPrime % 23 == 0:
            largestPrime = largestPrime / 23
        while largestPrime % 29 == 0:
            largestPrime = largestPrime / 29
        while largestPrime % 31 == 0:
            largestPrime = largestPrime / 31
        while largestPrime % 37 == 0:
            largestPrime = largestPrime / 37
        while largestPrime % 41 == 0:
            largestPrime = largestPrime / 41
        while largestPrime % 43 == 0:
            largestPrime = largestPrime / 43
        while largestPrime % 47 == 0:
            largestPrime = largestPrime / 47
        while largestPrime % 53 == 0:
            largestPrime = largestPrime / 53
        while largestPrime % 59 == 0:
            largestPrime = largestPrime / 59