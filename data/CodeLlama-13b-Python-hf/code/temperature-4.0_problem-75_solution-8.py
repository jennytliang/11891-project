def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    is_prime = "True"
    check_prime = True 
    primes = []

    if a >= 1000: 
      return "False"
    elif  a < 100: 
      return "Not implemented"
    elif a % 100 >= 20 or a % 2 ==  0:
      return "Not possible"
    elif  a <=  5 * 5 * 6:
      prime_1 = 2 
      prime_6 = 5 # 3 * 5 
      prime__1 = prime_6 - 1  #3 * 5 = 
      return True  
