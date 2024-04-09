def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: even , odd =
	"""
    # pass
    even = 0
    odd = 0
    str_num = str(num)
    if len(str_num) == 1:
        if int(str_num) % 2 == 0:
            even = 1
        else:
            odd = 1
    else:
        for i in str_num:
            if int(i) % 2 == 0:
                even += 1
            else:
                odd += 1
    return (even, odd)


# Pybites solution


def even_odd_count1(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: even , odd =
	"""
    if num < 0:
        num *= -1
    even, odd = 0, 0
    while num > 0:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
        num //= 10
    return (even, odd)
