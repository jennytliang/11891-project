def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    
	Include these tokens in the code: fac , ans =
	"""
    """special_factorial(3), "48" """
    fac = 1
    if (n > 1):
        ans = 1
        for i in range(1, n):
            fac = 2*fac -1
       #print('Fac: ' + str(fac) +', i: '+ str(i))
        while (fac>0):
            ans *= fac
            fac = fac - 1
            #print(str(ans))
    else:
        ans = 1
    #print('Ans : ' + str(ans*1))
    return ans*1


def special_factorial_v2(n):
    """SpecialFactorial (Brazilian)

    Using a Python comprehension to build the factorial
    And multiplication
    """
    #return reduce(lambda num, fact: num * fact, [fac for fac in range(n,1,-1)], 1)*1
    factorial = [fac for fac in range(n,1,-1)]
    return reduce(lambda num, fact: num * fact, factorial, 1)*1
    #return product(factorial) # this is also valid!
    
    
# Test Cases:

import math

# Test.it('SpecialFactorial (Brazilian)')
# expected = 288
# Test.assert_equals(special_factorial(4),expected,"Should equal 288")
#print(str(special_factorial(10)))
#help(math.factorial)
