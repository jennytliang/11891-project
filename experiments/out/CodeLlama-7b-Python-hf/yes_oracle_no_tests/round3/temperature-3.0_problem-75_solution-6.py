def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: if a <=
	"""
    if a <= 100:
        for i in range(1, a):
            if is_prime(i) and is_prime(a/i):
                return True
        return False
    else:
        return "a must be less then 100"


def is_prime(a):
    """Write a function that returns true if the given number is prime and false otherwise.
    Example:
    is_prime(3) == True
    
	Include these tokens in the code: while not
	"""
    if a <= 1:
        return False
    else:
        for i in range(2, a):
            if a % i == 0:
                return False
        return True


def run_calculations():
    """
        This function should call is_multiply_prime function
        for the range of numbers from 20 to 50
        and print the required results.
        Example:
        is_multiply_prime(30) == True
        30 = 2 * 3 * 5
    """
    print("Calculating the multiplication of 3 prime numbers in the range of 20 to 50:")
    for i in range(20, 50):
        if is_multiply_prime(i):
            print(i, "=", " * ", sep="", end="")
            for j in range(1, i):
                if is_prime(j) and is_prime(i/j):
                    print(j, end=" * ")
            print("")
        else:
            print(i, "is not the multiplication of 3 prime numbers")


if __name__ == "__main__":
    run_calculations()
