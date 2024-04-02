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
    for i in str(num):
        if int(i) % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


# TEST
# print(even_odd_count(123))   # (1, 2)
# print(even_odd_count(-12))   # (1, 1)
# print(even_odd_count(0))     # (1, 0)
# print(even_odd_count(10))    # (2, 0)
# print(even_odd_count(-10))   # (2, 0)
# print(even_odd_count(100))   # (2, 2)
# print(even_odd_count(-100))  # (2, 2)
# print(even_odd_count(1000))  # (3, 1)
# print(even_odd_count(-1000)) # (3, 1)
# print(even_odd_count(100000))  # (3, 3)
# print(even_odd_count(-100000)) # (3, 3)
# print(even_odd_count(1000000))  # (4, 2)
# print(even_odd_count(-1000000)) # (4, 2)
# print(even_odd_count(10000000))  # (5, 1)
# print(even_odd_count(-10000000)) # (5, 1)
# print(even_odd_count(100000000))  # (6, 2)
# print(even_odd_count(-100000000)) # (6, 2)
