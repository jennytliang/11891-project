def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: if a <=
	"""
    prime = [2, 3, 5, 7]
    for i in prime:
        if a%i == 0:
            return True
    return False

if __name__ == '__main__':
    print(is_multiply_prime(30))
    print(is_multiply_prime(35))
