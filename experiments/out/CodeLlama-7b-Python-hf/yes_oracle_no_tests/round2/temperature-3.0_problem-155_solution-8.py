def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Do not include these tokens in the code: # Y OUR CO DE H ERE
	"""
    # WRITE YOUR CODE HERE
    countEven = 0
    countOdd = 0
    if(num < 0):
        num = abs(num)
    while(num > 0):
        digit = num % 10
        if(digit % 2 == 0):
            countEven += 1
        else:
            countOdd += 1
        num = num // 10
    return (countEven, countOdd)


# TEST
print("even_odd_count(-12) == (1, 1): " + str(even_odd_count(-12) == (1, 1)))
print("even_odd_count(123) == (1, 2): " + str(even_odd_count(123) == (1, 2)))
print("even_odd_count(12345) == (2, 3): " + str(even_odd_count(12345) == (2, 3)))
