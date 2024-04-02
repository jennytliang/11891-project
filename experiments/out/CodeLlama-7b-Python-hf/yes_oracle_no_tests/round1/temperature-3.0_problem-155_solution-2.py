def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: even , odd =
	"""
    # Lets create a list with all the digits of the number
    # Using the function divmod(number, 10)
    # The first number is the quotient of the division
    # The second number is the remainder of the division
    # We use the function divmod() to do this in one line
    # The list will be in reverse order
    # So we use the function reverse()
    num_list = list(reversed(list(divmod(num, 10) for _ in range(len(str(num))))))
    # We will use two counters
    # One for even numbers
    # One for odd numbers
    even = 0
    odd = 0
    # Loop through the list of digits
    for i in num_list:
        if i[1] % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd)


# Pybites solution


def even_odd_count1(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: even , odd =
	"""
    # Lets create a list with all the digits of the number
    # Using the function divmod(number, 10)
    # The first number is the quotient of the division
    # The second number is the remainder of the division
    # We use the function divmod() to do this in one line
    # The list will be in reverse order
    # So we use the function reverse()
    num_list = list(reversed(list(divmod(num, 10) for _ in range(len(str(num))))))
    # We will use two counters
    # One for even numbers
    # One for odd numbers
    even = 0
    odd = 0
    # Loop through the list of digits
    for i in num_list:
