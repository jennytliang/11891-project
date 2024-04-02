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
    max_prime = max(lst)
    lst_prime = []
    for i in lst:
        if i == max_prime:
            lst_prime.append(i)
    for i in lst_prime:
        if is_prime(i):
            lst_prime.append(i)
    lst_prime = list(set(lst_prime))
    lst_prime.sort()
    prime = lst_prime[-1]
    prime_digit = []
    while prime != 0:
        tmp = prime % 10
        prime_digit.append(tmp)
        prime = prime // 10
    prime_digit.reverse()
    return sum(prime_digit)

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True