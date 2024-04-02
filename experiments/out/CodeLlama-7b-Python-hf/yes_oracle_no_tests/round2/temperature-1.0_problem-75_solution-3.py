def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: if a <=
	"""
    for i in range(a,100):
        is_prime = True
        for x in range(i,100):
            if i%x == 0 and i%x != 0 :
                is_prime = False
            if i%x == 0 and i%x == 0 and x < i:
                break
        if not is_prime:
            for x in range()

    return is_prime
        
def number_of_steps(n):
	"""Write a function that for every number between 1 and n returns the number of necessary steps
	to move from 1 to n.
	Example:
	number_of_steps(10) -> [1, 1, 1, 1, 1, 2, 1, 1, 2, 2, 2]
	"""
    if n > 0 or n <= 80:
        return 
    