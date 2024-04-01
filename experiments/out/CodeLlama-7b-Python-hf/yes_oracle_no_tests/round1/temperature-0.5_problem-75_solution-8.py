def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: <=  1
	Do not include these tokens in the code: < 0 0
	"""

    if a  <= 1:
        return False
    i = 2
    while i * i <= a:
        if a % i == 0:
            a = a / i
            i = 2
        else:
            i += 1
    return a == 1

