def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: even , odd =
	"""
    even = 0
    odd = 0
    if num < 0:
        num = -num
    while num > 0:
        if num % 10 == 0:
            even += 1
        elif num % 10 != 0:
            odd += 1
        num = num // 10
    return odd, even


# print(even_odd_count(123))
# print(even_odd_count(-12))
# print(even_odd_count(12))
# print(even_odd_count(0))

def even_odd_count_2(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: even , odd =
	"""
    even = 0
    odd = 0
    if num < 0:
        num = -num
    while num > 0:
        if num % 10 == 0:
            even += 1
        elif num % 10 != 0:
            odd += 1
        num = num // 10
    return odd, even


# print(even_odd_count(123))
# print(even_odd_count(-12))
# print(even_odd_count(12))
# print(even_odd_count(0))

def even_odd_count_3(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: even , odd =
	"""
    even = 0
    odd = 0
    if num < 0:
        num = -num
    while num >