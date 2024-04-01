def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: even , odd =
	"""
    even = 0
    odd = 0
    flag = False
    for n in str(num):
        if int(n) % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd)


# print(even_odd_count(123))
# print(even_odd_count(-12))
