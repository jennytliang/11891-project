def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n ==
	"""
    # Initialize the count
    count = 0
    
    # If n is 1 then we have 10 numbers that start or end with 1
    if n == 1:
        return 10
    
    # If n is 2 then we have 9 numbers that start or end with 1
    elif n == 2:
        return 9
    
    # If n is 3 then we have 9 numbers that start or end with 1
    elif n == 3:
        return 9
    
    # If n is 4 then we have 8 numbers that start or end with 1
    elif n == 4:
        return 8
    
    # If n is 5 then we have 8 numbers that start or end with 1
    elif n == 5:
        return 8
    
    # If n is 6 then we have 7 numbers that start or end with 1
    elif n == 6:
        return 7
    
    # If n is 7 then we have 7 numbers that start or end with 1
    elif n == 7:
        return 7
    
    # If n is 8 then we have 6 numbers that start or end with 1
    elif n == 8:
        return 6
    
    # If n is 9 then we have 6 numbers that start or end with 1
    elif n == 9:
        return 6
    
    # If n is 10 then we have 5 numbers that start or end with 1
    elif n == 10:
        return 5
    
    # If n is 11 then we have 5 numbers that start or end with 1
    elif n == 11:
        return 5
    
    # If n is 12 then we have 4 numbers that start or end with 1
    elif n == 12:
        return 4
    
    # If n is 13 then we have 4 numbers that start or end with 1
    elif n == 13:
        return 4
    
    # If n is 14