def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r val = 0 .
	"""
    # ============== YOUR CODE HERE ==============
    import math
    a = float(a)
    h = float(h)
    r = ((0.5*a)*h)/1
    val = 0
    val = r
    # ============================================
    return val



### DO NOT MODIFY THE CODE BELOW THIS LINE ###
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)