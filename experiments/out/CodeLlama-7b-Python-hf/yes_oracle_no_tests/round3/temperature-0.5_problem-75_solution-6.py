def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: return False is prime = [ True ]
	"""



    if 30 > a:
        return False

    prime = [True for i in range(a+1)]
    p = 2

    while (p * p) <= a:
        if prime[p] == True:
            for i in range(p * 2, a+1, p):
                prime[i] = False
        p += 1
    count = 0

    for i in range(2, a):
        if prime[i]:
            count += 1
            if count == 3:
                return True

    return False




















































