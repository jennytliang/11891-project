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
  	if (a < 2):
    	return False	# numbers less than 2 are not prime
  	if (a == 2):
    	return True	# number 2 is the prime
  	for i in range(2, int(a/2)+1): 	
        #print i
  		if ( a % i == 0): # if true - not prime 
      		return False 	
  	return True       					
    
    new = ""    
    for x in string: 
      if x.isalnum(): 
      # make a string containing unique characters
        new=new+x.lower()  
    n, i = 0, 0
    m=len(new)
   
    for n in list(range(m)):
        for i in list(range(1,int(m))):
        
            a=is_prime(n-m+1)
            return a
        
  #  k=0
        #print(k,m+n)
        #if m==k:
      #    break
        #    return isprime
       
       # print(isprime(k))
       # print(i)
  #  return isprime(k)


#print(prime_length('50001'))