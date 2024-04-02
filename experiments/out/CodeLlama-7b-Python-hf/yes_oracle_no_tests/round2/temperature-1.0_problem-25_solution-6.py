from typing import List


def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    
	Do not include these tokens in the code: if n <= 0
	"""

    if n == 1:
        return()

    product=n
    primeFactors=[]
    
    while(product != 1):
        for i in range(2,product):
            if product%i ==0:
                product=product/i
                primeFactors.append(i)
                break
    return primeFactors

factorize(100)