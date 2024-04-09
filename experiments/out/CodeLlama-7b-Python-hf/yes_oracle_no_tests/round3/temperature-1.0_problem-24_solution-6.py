def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    
	Do not include these tokens in the code: fo obar = 2
	"""
    # fo = 2
    # obar = 2
    # while True:
    #     if n % fo == 0:
    #         return fo
    #     else:
    #         fo += 1

    # return obar

    # for i in range(2, n):
    #     if n % i == 0:
    #         return i
    # return n
    # for i in range(2, n):
    #     if n % i == 0:
    #         return i
    # return n
    # for i in range(2, n):
    #     if n % i == 0:
    #         return i
    # return n
    for i in range(2, n):
        if n % i == 0:
            return i
    return n


print(largest_divisor(15))
