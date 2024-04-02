def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: , odd
	"""

    # LABELS
    even = 0
    odd = 0

    # WRITE YOUR CODE HERE
    for x in str(num):
        if int(x) % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


# TEST
# print(even_odd_count(123456789))
# (5, 4)
# print(even_odd_count(1234567890))
# (6, 5)
# print(even_odd_count(-123456789))
# (5, 4)
# print(even_odd_count(-1234567890))
# (6, 5)
# print(even_odd_count(0))
# (1, 0)
