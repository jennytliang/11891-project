def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: even , odd =
	"""
    # TO DO: write your solution here
    even = 0
    odd = 0
    for i in str(num):
        if int(i) % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


# TESTS
# Test 1
print(even_odd_count(-12))
# (1, 1)

# Test 2
print(even_odd_count(123))
# (1, 2)

# Test 3
print(even_odd_count(1234567890))
# (5, 5)

# Test 4
print(even_odd_count(1010101010101010101))
# (10, 10)
