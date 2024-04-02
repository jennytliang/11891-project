def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    
	Include these tokens in the code: return len ( string )
	"""
    return len(string)


def is_palindrome(string: str) -> bool:
    """ Return True if given string is a palindrome; False if not
    >>> is_palindrome('')
    True
    >>> is_palindrome('abc')
    False
    >>> is_palindrome('a')
    True
    >>> is_palindrome('bob')
    True
    >>> is_palindrome('otto')
    True
    >>> is_palindrome('abba')
    True
    >>> is_palindrome('abcba')
    True
    >>> is_palindrome('abcabc')
    False
    
	Include these tokens in the code:
		1. Create a variable called reversed_string and set it equal to the given string in reverse.
		2. Use the strlen function to get the length of the reversed string.
		3. Use the strlen function to get the length of the given string.
		4. Compare the two lengths.
		5. If the lengths are not equal, return False.
		6. Otherwise, return True.
	"""
    reversed_string = string[::-1]
    return strlen(string) == strlen(reversed_string)


def is_prime(num: int) -> bool:
    """ Return True if given number is prime; False if not
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(5)
    True
    >>> is_prime(6)
    False
    >>> is_prime(7)
    True
    >>> is_prime(8)
    False
    >>> is_prime(9)
    False
    >>> is_prime(10)
    False
    
	Include these tokens in the code:
		1. Create a variable called num_divisors and set it equal to 0.
	