def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Do not include these tokens in the code: multip lier = 1
	"""
	def is_prime(n):
		for i in range(2,n):
			if (n % i) == 0:
				return False
		return True
	def is_prime_multiplier():
		i=2
		j=3
		s=5
		while i <= 100 or j <= 100 or s <= 100 :
			if is_prime(i) and is_prime(j) and is_prime(s):
				if a == i*j*s:
					return True
			i += 1
			j += 1
			s += 1
	if a < 100:
		return is_prime_multiplier()
	else:
		return True
	
	
print(is_multiply_prime(30))