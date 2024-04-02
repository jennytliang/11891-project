def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: even , odd =
	"""
    even, odd = 0, 0
    # your code here
    if num < 0:
        num = -num
    while num > 0:
        last_digit = num % 10
        if last_digit % 2 == 0:
            even += 1
        else:
            odd += 1
        num //= 10
    return even, odd

print(even_odd_count(123))
print(even_odd_count(-12))
print(even_odd_count(100))
print(even_odd_count(0))