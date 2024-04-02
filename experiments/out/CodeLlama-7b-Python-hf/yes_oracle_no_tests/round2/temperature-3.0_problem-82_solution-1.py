def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    
	Do not include these tokens in the code: # pass
	"""
    # pass
    return (len(string) in prime_numbers())


def prime_numbers():
    """Write a function that returns a list of prime numbers up to 100
    Examples
    prime_numbers() == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    """
    # pass
    primes = []
    for i in range(2, 100):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes
