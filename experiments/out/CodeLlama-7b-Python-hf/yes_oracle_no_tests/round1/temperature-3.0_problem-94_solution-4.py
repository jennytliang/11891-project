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
        if a < 2:
            return False
        for i in range(2, a):
            if a % i == 0:
                return False
        return True

    lst_new = []
    for i in lst:
        if i > 0 and is_prime(i):
            lst_new.append(i)
    lst_new.sort(reverse=True)
    print("lst_new", lst_new)
    prime_num = lst_new[0]
    print("prime_num", prime_num)
    sum_of_digits = sum([int(i) for i in str(prime_num)])
    return sum_of_digits
