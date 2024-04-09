def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: : return False is prime = [ True
	"""


    if 0 < a < 100:
        n = a
        for i in range(2, int(n/2)+1):
            if n % i == 0:
                if is_prime(i) == True:
                    n = n/i
                    if n == 1:
                        return True
                    else:
                        continue
                else:
                    return False
            else:
                continue
    else:
        return False


def is_prime(n):
    """Write a function that returns true if the given number is prime
    and false otherwise.
    Knowing that (n) is less then 100.
    Example:
    is_prime(7) == True
    is_prime(71) == False
    """

    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
            else:
                continue
        return True


if __name__ == "__main__":
    print(is_multiply_prime(30))
    print(is_prime(30))
