def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: even , odd =
	Do not include these tokens in the code: # Y OUR CO DE H
	"""
    # pass
    # YOUR CODE HERE
    even = 0
    odd = 0
    for i in str(abs(num)):
        if int(i) % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


print(even_odd_count(-12))
print(even_odd_count(123))
