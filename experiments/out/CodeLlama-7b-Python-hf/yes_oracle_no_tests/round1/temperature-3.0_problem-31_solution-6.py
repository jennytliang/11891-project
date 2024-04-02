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
    
	Do not include these tokens in the code: if
	"""

    if n <= 1: return Fals
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


#----------------------------------------------------------------
# Problem 2:
# The following code raises a TypeError.
# Why does it raise a TypeError?
# Try to fix the code so that it prints the numbers 10 through 20,
# inclusive, one per line.

for i in range(10, 21):
    print(i)

#----------------------------------------------------------------
# Problem 3:
# The following code raises a SyntaxError.
# Fix the code so that it's a valid Python expression.

print "Hello, world!"

#----------------------------------------------------------------
# Problem 4:
# The following code raises a SyntaxError.
# Fix the code so that it's a valid Python expression.

print "Hello, world!"

#----------------------------------------------------------------
# Problem 5:
# The following code raises a TypeError.
# Fix the code so that it's a valid Python expression.

print "Hello, world!"

#----------------------------------------------------------------
# Problem 6:
# The following code raises a TypeError.
# Fix the code so that it's a valid Python expression.

print "Hello, world!"

#----------------------------------------------------------------
# Problem 7:
# The following code raises a TypeError.
# Fix the code so that it's a valid Python expression.

print "Hello, world!"

#----------------------------------------------------------------
# Problem 8:
# The following code raises a ValueError.
# Fix the code so that it's a valid Python expression.

print "Hello, world!"

#----------------------------------------------------------------
# Problem 9:
# The following code raises a NameError.
# Fix the code so that it's a valid Python expression.

print "Hello, world!"

#----------------------------------------------------------------
# Problem 10:
# The following code raises a SyntaxError.
# Fix the code so that it's a valid Python expression.

print "Hello, world!"

#----------------------------------------------------------------
# Problem 11: