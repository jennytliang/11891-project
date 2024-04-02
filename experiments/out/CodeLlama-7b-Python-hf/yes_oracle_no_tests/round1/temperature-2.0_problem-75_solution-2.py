def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: <=
	Do not include these tokens in the code: >
	"""

    # ------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    # ------------------------------------------------------------------

    # ------------------------------------------------------------------
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      5
    #    TIME ESTIMATE:   5 minutes.
    # ------------------------------------------------------------------

    for j in range(2,a):
        for i in range(2,j):
            if a%i == 0 and is_prime(i):
                return True
    return False



def is_prime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True






















