def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Do not include these tokens in the code: 0 0
	"""

    
    #a=str(a)
    b=set()
    for i in range(2, int(a**(1/3))+1):
        c=0
        primes=[]
        if a%i==0:
            primes.append(i)
            x, y = divmod(a, i)
            #print(x,y)
            for j in range(2, int((int(a/i)**(1/3))+1)):
                if y%j==0:
                    #print(j)
                    #print(y)
                    if j in b and x in b:
                        c+=1
                    b.add(j)
                    x,y=divmod(x,j)
            #print(c)
            if c == 1:
                #print(primes)
                return True
    return False

is_multiply_prime(30)