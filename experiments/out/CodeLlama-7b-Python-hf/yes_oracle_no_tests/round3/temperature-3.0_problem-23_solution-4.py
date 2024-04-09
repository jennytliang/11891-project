def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    
	Include these tokens in the code: return len ( string )
	"""
    return len(string)


def is_palindrome(word: str) -> bool:
    """ Return whether given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('a')
    True
    >>> is_palindrome('aa')
    True
    >>> is_palindrome('ba')
    False
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('abcba')
    True
    >>> is_palindrome('abcabc')
    False
    
	Include these tokens in the code:
	1. Convert the string to lowercase
	2. Loop through the string
	3. Check if the first character is equal to the last character
	4. If they are not equal, return False
	5. If they are equal, remove the first and last characters
	6. Repeat steps 2, 3, and 4 until you have checked all characters in the string
	7. Return True
	"""
    word = word.lower()
    for i in range(len(word)):
        if word[i] != word[len(word) - i - 1]:
            return False
    return True


def gcd(a: int, b: int) -> int:
    """ Return the greatest common divisor of a and b using Euclid's Algorithm
    >>> gcd(12, 16)
    4
    >>> gcd(2, 3)
    1
    >>> gcd(0, 8)
    8
    >>> gcd(7, 9)
    1
    
	Include these tokens in the code:
	1. If a is zero, return b
	2. If b is zero, return a
	3. Set a_temp to a
	4. Set b_temp to b
	5. While a_temp is not equal to b_temp
	6. If a_temp is greater than b_temp
	7. Set a_temp to a_temp minus b_temp
	8. Else
	9. Set b_temp to b_temp minus a