def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    
	Include these tokens in the code: import random def mill er _ ra bin
	Do not include these tokens in the code: fib = [ 1 , 1
	"""
    if n==0:
        return 2
    if n<=2:
        return 3

    fibonacci=[1,1]
    
    while(len(fibonacci)<n):
        fibonacci.append(fibonacci[len(fibonacci)-1]+fibonacci[len(fibonacci)-2])
    list_fib=[]
    for i in fibonacci[2:len(fibonacci)]:
        if miller_rabin_(i):
            list_fib.append(i)
        for i in list_fib:
            list_fib.insert(1,i) 
    return list_fib
    
def miller_rabin_(num):
	"""
	miller_rabin_ will return true if prime, otherwise false.
	"""
	#  if no_of_calls==20:
		#  return false

	#  return miller_rabin_(num//9)^2 + (miller_rabin_(num//3)^4) - miller_rabin_(num)^(8*miller_rabin_(num)^4)-(miller_rabin_(num//3)^4) + (miller_rabin_(num//9)^2))
    def miller_rabin_(n):
		"""
		miller_rabin_ will return true if prime, otherwise false.
		"""
        if n==2:
            return True
        if n==1 or n==3 or n==5 or n==7 or n==9:
            return True
        if n<=3:
            return False
        n=n//9
        ans1=miller_rabin_(n)
        n=n//3
        ans2=miller_rabin_(n)
        ans3=miller_rabin_(n*n)
        n=n*9
        ans4=miller_rabin_(n)
        n=n//3
        
        ans5=miller_rabin_(n)
        if ans1==False or ans2