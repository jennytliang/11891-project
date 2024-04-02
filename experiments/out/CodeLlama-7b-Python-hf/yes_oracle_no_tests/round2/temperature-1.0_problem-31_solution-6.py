def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    
	Include these tokens in the code: n _ sqrt
	Do not include these tokens in the code: d
	"""

    if n <= 1: return Fals
    for i in i_list:
        if n % i == 0: return False
    return True

def make_table(n):
    """ Return a list such that the ith element 
        is the product of the integers from 1 
        to i.  The list should have n elements.
    """
        

def make_nCr(n, r):
    pass
    


# tests with nose
def check_extra_credit():
    """ Write code a test case.
    
    Run nose by typing in terminal: 
    nose exercise10.py 
    """