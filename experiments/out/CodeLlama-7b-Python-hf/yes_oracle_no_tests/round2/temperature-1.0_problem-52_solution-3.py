def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Include these tokens in the code: return all ( x < t for x in l
	"""
    return all(x < t for x in l)

def below_threshold_two(l, t):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
     True
    >>> below_threshold([1, 20, 4, 10], 5)
     False
    
    Add only one return statement
    """
    for x in l:
        if x >= t:
            return False
    return False

def below_threshold_three(l,t):
    """Return True if all numbers in the list l are below threshold t.
         >>> below_threshold([1, 2, 4, 10], 100)
   		  True
   		  >>> below_threshold([1, 20, 4, 10], 5)
   		  False
    """
    for x in l:
        if x >= t:
            return False
    return True

from random import randint
def silly(n):
    """Return a list of n randomly generated integer which have one or more
    properties which are inconsistent with each other:
        1. all numbers in the list are below threshold 10
        2. The last element of the list is a multiple of 2 and 3
        3. The sum of all numbers is odd.
    >>> silly(10)
    [4, 6, 7, 7, 1, 10, 5, 8, 8, 6]
    """
    
    result = []
    while len(result) < n:
        x = randint(0,9)
        if x < 10:
            if x >= 2 and x%6 == 0:
                result.append(x)

    if result[-1] % 6 == 0 and result[-1]%2 ==0:
        result[0] = randint(0,9)
    return result

if __name__ == "__main__":
    import do