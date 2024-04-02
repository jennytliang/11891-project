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
        # here write your code
        
        for i in range(2, (a//2) + 1):
            # print(a%i)
            if a % i == 0:
                if i > 1:
                    found_prime = True
                    j = 2
                    while found_prime == True and j < i:
                        found_prime = True
                        if i % j == 0:
                            found_prime = False
                        j += 1
                    if found_prime == True:
                        return True
    
        return False
    
    else:
        return -1 #a is greater then 100
    
def is_square_multiply_prime(a):
    """Write a function that returns true
    if the given number is the multiplication of 3 prime numbers,
    each prime number is squared and false otherwise.
    Knowing that (a) is less then 100. 
    Hint: you should use 2 ** (1/2)
    Example:
    is_square_multiply_prime(9) == True
    9 = (2 ** 2) * (3 ** 2)
    """
    
    if a <= 100:
        found_prime = True # 
        i = 2
        while found_prime == True and i * i <= a:
            i += 1
            found_prime = False
            j = 2
            while found_prime == False and j * j <= i:
                found_prime = True
                if (i % j) == 0:
                    found_prime = False
                j += 1
            
        if found_prime == True:
            return True
        else:
            return False
    
    else:
        return -1 #a is greater then 100
    
def is_multiply_square_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers,
    each prime number is raised to the power of 2 and false if otherwise.
