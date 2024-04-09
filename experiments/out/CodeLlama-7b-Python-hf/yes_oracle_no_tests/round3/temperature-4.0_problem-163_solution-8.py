def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    
	Do not include these tokens in the code: # Y OUR CO DE H ERE
	"""
    #pass
    # BEGIN PROBLEM 1
    result = []
    if a > b:
        a, b = b, a
    for i in range(a, b + 1):
        if i % 2 == 0:
            result.append(i)
    return result
    # END PROBLEM 1

def is_palindrome(s):
    """
    Given a string, return True if the string is a palindrome.
    
    Do not use Python's reverse string method.
    
    For example:
    is_palindrome('noon') returns True
    is_palindrome('raindrome') returns False
    is_palindrome('racecar') returns True
    
	Do not include these tokens in the code: # Y OUR CO DE H ERE
	"""
    #pass
    # BEGIN PROBLEM 2
    if len(s) == 0:
        return True
    elif len(s) == 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False
    # END PROBLEM 2

def gcd(a, b):
    """
    Given two positive integers a and b, return the greatest common divisor
    of a and b using recursion.
    
    Do not use Python's greatest common divisor function.

    For example:
    gcd(6, 9) returns 3
    gcd(2, 3) returns 1
    gcd(3, 6) returns 3
    
	Do not include these tokens in the code: # Y OUR CO DE H ERE
	"""
    #pass
    # BEGIN PROBLEM 3
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    # END PROBLEM 3

def summation(n, term):
    """
    Given a term and a number n, return the sum of the first n terms