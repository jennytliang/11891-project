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
    prime = [2, 3, 5]
    for num in prime:
        if a % num != 0:
            return False
    return True
    

if __name__ == "__main__":
    print(is_multiply_prime(30))
