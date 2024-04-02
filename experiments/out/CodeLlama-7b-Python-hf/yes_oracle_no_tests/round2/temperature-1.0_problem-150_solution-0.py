def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    
	Include these tokens in the code: def is _ prime ( a ): return
	"""
    if is_prime(n) is True:
        return x
    else:
        return y




is_prime = 0

def prime_nums(n):
    """
    return a list of all prime numbers up to and including n, ordered.
    For example, prime_nums(10) should return [2, 3, 5, 7].
    Hint: n is greater than or equal to 2.
    """

    # this list will hold all the prime numbers of range n
    listOfPrimes = []  

    # loop through each number to test if it is prime
    for i in range(2,n+1): # loop through 2 to limit the numbers that need to be checked

        # check if i is prime and add to list if it is a prime number
        if is_prime(i) is True: 
            listOfPrimes.append(i)

    # return the list with all of the prime numbers up to n
    return listOfPrimes