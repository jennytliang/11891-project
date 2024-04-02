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
	Do not include these tokens in the code: pass # F ill here
	"""
    from math import sqrt
    
    p = 0
    f = 1
    i = 1
    while True:
        p2 = p*p + f*f
        pi = int(sqrt(p2))
        f2 = 4*p*f + 3*f*f
        fi = int(sqrt(f2))
        i += 2

        if(p2 % 2 == 0):
            if (pi == f2):
                break
        elif(f2 % 2 ==0):
            if (fi == p2):
                break
        else:
            if (fi != p2):
                break

        p = f
        f = f2
    # Fill your code here!
    return n

def main():
    print(prime_fib(10))
    
if __name__=="__main__":
    main()