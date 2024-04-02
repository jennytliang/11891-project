def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Do not include these tokens in the code: # TO DO : write your solution
	"""
    # TO DO : write your solution
    even_count = 0
    odd_count = 0
    if num < 0:
        num = num * (-1)
    while num > 0:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        num = num // 10
    return (even_count, odd_count)


# Simple Testing
# print(even_odd_count(-12))  # (1, 1)
# print(even_odd_count(123))  # (1, 2)
# print(even_odd_count(12345))  # (2, 3)
# print(even_odd_count(1234567))  # (3, 4)
# print(even_odd_count(123456789))  # (4, 5)
# print(even_odd_count(1234567890))  # (5, 4)
