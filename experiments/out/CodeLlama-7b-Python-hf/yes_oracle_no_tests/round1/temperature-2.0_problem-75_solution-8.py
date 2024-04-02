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
    # DONE: 3. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    # ------------------------------------------------------------------
    # ------------------------------------------------------------------
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      7
    #    TIME ESTIMATE:   5 minutes.
    # ------------------------------------------------------------------

    count = 0
    for k in range(1, 100):
        if is_prime(k) == True:
            count = count + 1
    if count == 3:
        return True
    else:
        return False


def is_prime(a):
    count = 0
    for k in range(1, a + 1):
        if a % k == 0:
            count = count + 1
    if count == 2:
        return True
    else:
        return False
