def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: even , odd =
	"""
    if num < 0:
        num = -num
    even = 0
    odd = 0
    while num:
        if num % 10:
            odd += 1
        else:
            even += 1
        num //= 10
    return (even, odd)



print(even_odd_count(-12))
print(even_odd_count(123))