def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: even , odd =
	"""
    # YOUR CODE HERE
    even = 0
    odd = 0
    count = 0
    num_string = str(abs(num))
    for i in num_string:
        count += 1
        if int(i) % 2 == 0:
            even += 1
        else:
            odd += 1
    if num < 0:
        even, odd = odd, even
    return (even, odd)


# TESTS
assert even_odd_count(123) == (1, 2)
assert even_odd_count(-1234) == (2, 2)
assert even_odd_count(1230) == (2, 1)
assert even_odd_count(-1) == (0, 1)
assert even_odd_count(0) == (1, 0)
