def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: if a <=
	"""
    pass
    numbers=set()
    for i in range(2,a+1):
        n=i
    
    while n<=a:
        if a%n==0:
            numbers.add(n)
            print(numbers)

        n+=1
        # print(numbers)        
    return len(numbers)==3

print(is_multiply_prime(24))