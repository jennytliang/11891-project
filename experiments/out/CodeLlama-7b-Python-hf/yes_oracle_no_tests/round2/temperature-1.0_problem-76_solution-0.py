def is_simple_power(x, n):
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    
	Do not include these tokens in the code: assert ( x >= 0 and n
	"""
    # Simple Test
    y = True
    if n == 0 and y != 0:
        print('Is it not zero???')

    return (x**y) == n



    # Simple Solution
    #    """Returns True if the positive integer x is a power of the integer n.'''
    #    Args:
    #        x (int): A positive integer
    #        n (int): An integer
    #    Returns:
    #        bool: True if x is a power of n
    #    """
    #    return (n == 1) or (x == n and n != 0) or ((x % n == 0) and is_simple_power(x // n, n))
    #



    # Simpler Solution
    #    
    #    def is_pow(x, n):
    #        '''
    #        Return True if x is n's exponent, and False otherwise.
    #        '''
    #       # Base Case
    #        if n == 1:
    #            return True
    #        
    #       # Inductive Hypothesis
    #        elif x % n == 0:
    #            return is_pow(x // n, n)
    #        else: 
    #            return False
    #            
    #    # Test Code
    #    print(is_pow(27, 3))
    #    print(is_pow(5, 2)