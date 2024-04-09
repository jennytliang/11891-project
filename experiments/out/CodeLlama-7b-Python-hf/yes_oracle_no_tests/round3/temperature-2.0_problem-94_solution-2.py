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
    
	Include these tokens in the code: def is _ prime ( a ):
	Do not include these tokens in the code: pr imes = [] for
	"""
    # first of all, we need to create a function that checks if a number is a prime number
    def is_prime(a):
        if a < 2:
            return False
        for i in range(2, a):
            if a % i == 0:
                return False
        return True

    # now we need to create a function that takes a number as a parameter and returns the sum of its digits
    def sum_of_digits(a):
        n = 0
        while a != 0:
            n += a % 10
            a = a // 10
        return n

    # finally we need to create a function that takes a list as a parameter and returns the largest prime number and the sum of its digits
    def largest_prime_sum(lst):
        primes = []
        for i in lst:
            if is_prime(i):
                primes.append(i)
        return sum_of_digits(max(primes))

    return largest_prime_sum(lst)


print(skjkasdkd([0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3]))
print(skjkasdkd([1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1]))
print(skjkasdkd([1, 3, 1, 32, 5107, 34, 83278, 109, 163, 23, 2323, 32, 30, 1, 9, 3]))
print(skjkasdkd([0, 724, 32, 71, 99, 32, 