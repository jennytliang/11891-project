def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    
	Include these tokens in the code: return not ( a
	Do not include these tokens in the code: if
	"""

    def is_prime(a):
  
      for i in range(2,a):
        if (a % i) == 0:
          return False
      else:
        return True
    
    if len(string) == 0:
      return False
    elif len(string) == 1:
      return True
    elif len(string) == 2:
      return True
    elif len(string) > 2:
      return is_prime(len(string))


print(prime_length('Hello'))
print(prime_length('abcdcba'))
print(prime_length('kittens'))
print(prime_length('orange'))
print(prime_length(''))
print(prime_length('1'))
print(prime_length('2'))
print(prime_length('3'))
print(prime_length('4'))
print(prime_length('5'))
print(prime_length('6'))
print(prime_length('7'))
print(prime_length('8'))
print(prime_length('9'))