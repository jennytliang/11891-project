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
        list_of_prime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
        for i in list_of_prime:
            if a % i == 0:
                number_of_factors = 0
                for j in list_of_prime:
                    if a % j == 0:
                        number_of_factors += 1
                        if number_of_factors == 3:
                            return True
                if number_of_factors == 2:
                    return True
        return False
    return 'Error'


def run_avg(arr):
    """Write a function that returns the moving average of a list
    Example:
    run_avg([75, 64, 66, 67, 68, 69, 70, 71, 72]) == 70
    run_avg([75, 64, 66, 67, 68, 69, 70, 71, 72, 73]) == 71.5
    """
    return sum(arr) / len(arr)


def is_prime(a):
    """Write a function that returns true if the given number is prime and false otherwise.
    Knowing that a is an integer between 0 and 100.
    Example:
    is_prime(7) == True
    is_prime(13) == True
    is_prime(99) == True
    is_prime(87) == False
    is_prime(12) == False
    """
    if a <= 100:
        if a == 2 or a == 3 or a == 5 or a == 7:
            return True
        if a % 2 == 0 or