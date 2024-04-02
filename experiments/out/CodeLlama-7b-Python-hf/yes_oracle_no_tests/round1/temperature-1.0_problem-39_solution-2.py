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
	Do not include these tokens in the code: if n == 1 :
	"""
    m = 1
    res=0
    while m<n:
        m,res=res,res+1
        nt=1
        while nt*(nt+1)<=2*res:
            if res%nt==0 and res%(nt+1)==0:
                break
            
            nt+=1
        if nt*(nt+1)>res and res%2!=0:
            n-=1
            m,res=res,res+1
    return 2*res

if __name__ == "__main__":
    import doctest
    doctest.testmod()