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
    else: 
        for i in range(2,101):
            if a % i == 0:
                if is_prime(i) == True:
                    a = a / i
                    if is_prime(a) == True:
                        return True
    return False

def is_prime(a):
    """Write a function that returns true if the given number is prime and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_prime(3) == True
    3 is prime
    
	Include these tokens in the code: <=  1
	Do not include these tokens in the code: < 0 0
	"""

    if a <= 1:
        return False
    else:
        for i in range(2,a):
            if a % i == 0:
                return False
        return True


def is_prime_with_list(a):
    """Write a function that returns true if the given number is prime and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_prime(3) == True
    3 is prime
    
	Include these tokens in the code: <=  1
	Do not include these tokens in the code: < 0 0
	"""
    prime_list = [2]
    if a <= 1:
        return False
    else:
        for i in range(3,a+1,2):
            is_prime = True
            for prime in prime_list:
                if i % prime == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_list.append(i)
    return True if a in prime_list else False


if __name__ == "__main__":
    print(is_multiply_prime(30))
    print(is_prime(3))
    print(is_prime_with_list(3))
