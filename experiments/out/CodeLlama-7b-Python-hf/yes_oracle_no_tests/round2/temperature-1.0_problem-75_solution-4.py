def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Do not include these tokens in the code: # check if number is less then
	"""
    if a > 100:
        return False

    if a % 2 == 0 or a % 3 == 0:
        return False

    count = 1
    while a % 2 == 0:
        count += 1
        a /= 2
    while a % 3 == 0:
        count += 1
        a /= 3
    while a % 5 == 0:
        count += 1
        a /= 5
    while a % 7 == 0:
        count += 1
        a /= 7
    while a % 11 == 0:
        count += 1
        a /= 11
    return (a == 1 or count < 4)
