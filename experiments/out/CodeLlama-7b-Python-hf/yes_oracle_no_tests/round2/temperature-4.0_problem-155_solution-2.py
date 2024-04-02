def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: , odd
	"""

    # pass
    even = 0
    odd = 0
    if num < 0:
        num = num * -1
    while num > 0:
        if num % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1
        num = num // 10
    return even, odd


# TEST
temp = even_odd_count(123)
print(temp)
temp = even_odd_count(-12)
print(temp)
temp = even_odd_count(1230)
print(temp)
temp = even_odd_count(-120)
print(temp)
temp = even_odd_count(12300)
print(temp)
temp = even_odd_count(-1200)
print(temp)
temp = even_odd_count(0)
print(temp)
temp = even_odd_count(-0)
print(temp)
temp = even_odd_count(1)
print(temp)
temp = even_odd_count(-1)
print(temp)
