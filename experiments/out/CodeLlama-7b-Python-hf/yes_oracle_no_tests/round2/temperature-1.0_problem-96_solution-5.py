def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    count_up_to(5) => [2,3]
    count_up_to(11) => [2,3,5,7]
    count_up_to(0) => []
    count_up_to(20) => [2,3,5,7,11,13,17,19]
    count_up_to(1) => []
    count_up_to(18) => [2,3,5,7,11,13,17]
    
	Include these tokens in the code: is prime = [ True ] * (
	"""

    
  
    def validate_prime(x):
        if x<2:
            return ""
        for i in range (2, x):
            if x % i == 0:
                # The number is divisible by i, not a prime number
                return ""
        return x
    

    
    
    primes = [ "", ] * n
    
    for i in range (1, n+1):
        num = validate_prime(i)
        if num != "":    
            primes[i-1]= str(num)
            
    return primes


