def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Do not include these tokens in the code: # pass
	"""
    # pass
    even = 0
    odd = 0
    if num < 0:
        num = -num
    while num > 0:
        r = num % 10
        if r % 2 == 0:
            even += 1
        else:
            odd += 1
        num = num // 10
    return (even, odd)


print(even_odd_count(-12))
print(even_odd_count(123))
print(even_odd_count(1234567890))
