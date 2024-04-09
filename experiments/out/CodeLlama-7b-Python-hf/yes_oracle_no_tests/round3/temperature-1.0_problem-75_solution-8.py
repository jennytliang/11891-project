def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: if a <=
	"""
    if a <= 100:
        if a == 2:
            return True
        elif a == 3:
            return True
        elif a == 5:
            return True
        elif a == 7:
            return True
        elif a == 11:
            return True
        elif a == 13:
            return True
        elif a == 17:
            return True
        elif a == 19:
            return True
        elif a == 23:
            return True
        elif a == 29:
            return True
        elif a == 31:
            return True
        elif a == 37:
            return True
        elif a == 39:
            return True
        elif a == 41:
            return True
        elif a == 43:
            return True
        elif a == 47:
            return True
        elif a == 53:
            return True
        elif a == 59:
            return True
        elif a == 61:
            return True
        elif a == 67:
            return True
        elif a == 71:
            return True
        elif a == 73:
            return True
        elif a == 79:
            return True
        elif a == 83:
            return True
        elif a == 89:
            return True
        elif a == 97:
            return True
        else:
            return False
    else:
        return False


def run_avg_list(values):
    """Write a function that receives a list of numbers and returns the average of the numbers.
    Example:
    run_avg_list([1, 2, 3, 4, 5]) == 3
    run_avg_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5.5
    
    Knowing that the length of the list is always even.
    """
    sum = 0
    for i in values:
       