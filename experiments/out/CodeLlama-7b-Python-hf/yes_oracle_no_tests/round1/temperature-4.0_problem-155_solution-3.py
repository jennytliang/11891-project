def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: even , odd =
	"""
    even = 0
    odd = 0
    for i in str(num):
        if int(i) % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


# print(even_odd_count(-12))
# print(even_odd_count(123))

def even_odd_count_2(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: even , odd =
	"""
    even = 0
    odd = 0
    for i in str(num):
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


# print(even_odd_count_2(-12))
# print(even_odd_count_2(123))

def even_odd_count_3(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: even , odd =
	"""
    even = 0
    odd = 0
    for i in str(num):
        if int(i) % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


# print(even_odd_count_3(-12))
# print(even_odd_count_3(123))

def even_odd_count_4(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_