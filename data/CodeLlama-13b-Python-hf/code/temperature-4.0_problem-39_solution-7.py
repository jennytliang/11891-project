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
    """
    a, b = 1, 1
    fib_iter = 0
    while len(primeFactors(b)) > 2 or any(
        j != 1 and b == j*(j+1)
        for i in [a, b] for j in primeFactors(i) ):
        a = b
        b += a
        fib_iter += 1   
    if fib_iter + 1 == n or fib_iter == n :
        # we need to take the next first fibonacci not to add the first one
        return b+a 
    elif fib_iter > n:
        # return n-th fibonacci if the iteration had passed already 
        return b-a
    else:
        # this is our loop where we continue to find the n-th prime Fibonacci numbers

        # we add one just to check if there is a next prime Fib numbers
        fib_iter += 1   

        while not (len(primeFactors(b)) == 2 or (any(j**2 - j*a -1 ==0 for j in  primeFactors(a) ) and any(k > 1 and b == k*(b+k) 
            for i in [b, b+1, b+2] 
                for k in primeFactors(i)
           ))):
            # this if checks all the above requirements that the n-th prime fib numbers must have just two prime factors.

            # to do so we need to use all these conditionals. 

                # if the nth number of fib numbers has prime factors equal to 2, it means we need the following form to make it prime
                 # 1. it must have more than two prime number factors (to ensure we don not have just one) we use: 2*3 or similar
                # 2. any prime factor (a b) that divided the a-th prime fib number must satisfy that:
                 #  i. (b**2-a*b-1)) % a must == 0
                 #  ii. b % 2 == 2 
                 #  iii, b*(b+1) == b

            a = b
            # a is set as the last b (b+a in the below line
            b += a
            fib_iter +=1 
        # we have now found the value of the desired number b, to print it in fib form we return a tuple (b-a, b) as:
       
        #  b is Fib(n) where b = Fib(n) + Fib(n-1)
        # so a = FIB(n-1)

# we need this list of prime numbers in the next loop for the prime factor search
    primes = primesbelow(n)

    while not(  (b % 2 == 1 and all(b % i !=0 for i in [ 2, *primes[:len(primeFactors(b))] ]))  or (b in primes) or b == 2 ):
        a = (b - a)
            # this will continue iteratively till the previous a value gives a prime b value and we continue this loop in order to find the
            #  biggest prime b and corresponding a value and stop when we are satisfied that the current prime b and its previous prime b will
            # meet the requirements of prime factoring, so the current b and its previous must have one prime factor only.

        b -= a
            # if they do not meet, we will continue to decrease the prime (current b to its previous prime b), till we find when this prime b meets
            # the requirements, which means that in the below loop we find that the next prime b that we set in the a variable will also be a prime b
            # but the a in the first loop is set the b in the same loop so it might be a problem in our search if a is not a prime as it is 
             # when the loop ends

    return a      


# helper functions to check if number a is prime and to find the prime factor of the number n 
def factor_find(n: int):
    num = 1  
    factors = 0  # will represent the prime factor number
    for i in range(n): 
        # since we need an iteration to find factors
        i += 1 
        if n % i == 0: # check first whether the modulo is zero to check if n has an integer factor
             factors = i
    # after the loop has completed, we then check if this factor is the number itself which represents that the number is a prime number
     if factors == i and n != i: # if it is this number is not prime and so the number itself should be returned to continue searching for a
        # factor 

         num = f'{n=}, {num =}, not prime' if (n != 5) else 2
     return num, factors
         
