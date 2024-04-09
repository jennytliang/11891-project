def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: even , odd =
	Do not include these tokens in the code: if num <
	"""
    even = 0
    odd = 0
    if num == 0:
        even += 1
    else:
        while num > 0:
            if num % 10 == 0:
                even += 1
            elif num % 10 != 0:
                odd += 1
            num = num // 10

    return even, odd
