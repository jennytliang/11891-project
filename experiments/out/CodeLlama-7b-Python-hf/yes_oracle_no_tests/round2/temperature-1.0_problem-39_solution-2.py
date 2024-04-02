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
	Do not include these tokens in the code: m = 1 res
	"""
   
    first = 2
    second = 3
    while second<n:
        first,second = second,first+second  
    return second
     
def main():
    print (prime_fib(1000))   

if __name__ == '__main__':
    main()
