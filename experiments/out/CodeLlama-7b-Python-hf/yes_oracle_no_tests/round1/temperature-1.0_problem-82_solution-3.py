def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    
	Include these tokens in the code: def is _ prime ( a ):
	"""
    import math
 
    def prime(nbr):
      i = 2
      if(nbr<2):
        return 0
      while (i<nbr/2):
        if(nbr%i==0):
          return 0
        i += 1
      return 1
   
    if prime(len(string)) == 1:
        return True
    return False

