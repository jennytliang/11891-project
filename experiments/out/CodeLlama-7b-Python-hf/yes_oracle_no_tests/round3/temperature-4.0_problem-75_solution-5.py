def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: <=
	Do not include these tokens in the code: ==
	"""


   #Write your code here
    for i in range(1,100):
        if a%i==0:
            for j in range(1,100):
                if a%j==0:
                    for k in range(1,100):
                        if a%k==0:
                            return True
    return False


print(is_multiply_prime(10))
print(is_multiply_prime(30))
print(is_multiply_prime(75))
print(is_multiply_prime(125))
print(is_multiply_prime(127))
print(is_multiply_prime(126))



def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: <=
	Do not include these tokens in the code: ==
	"""


   #Write your code here
    for i in range(1,100):
        if a%i==0:
            for j in range(1,100):
                if a%j==0:
                    for k in range(1,100):
                        if a%k==0:
                            return True
    return False


print(is_multiply_prime(10))
print(is_multiply_prime(30))
print(is_multiply_prime(75))
print(is_multiply_prime(125))
print(is_multiply_prime(127))
print(is_multiply_prime(126))

