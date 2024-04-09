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
    """ Return True if given string is palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('abc')
    False
    >>> is_palindrome('abba')
    True
    >>> is_palindrome('abbc')
    False
    
	Include these tokens in the code: 
		1.  Create a new string that is the reverse of the given string
		2.  Compare the two strings
		3.  Return True if the strings are equal
    
	"""
    return string == string[::-1]


def is_member(a: float, v: list) -> bool:
    """ Return True if a is a member of v
    >>> is_member(3, [1, 2, 3, 4])
    True
    >>> is_member(5, [1, 2, 3, 4])
    False
    
	Include these tokens in the code: 
		1.  Create a new list that is a copy of v
		2.  Use a while loop to check each element in the list
		3.  If an element is equal to a, return True
		4.  Otherwise, return False
    
	"""
    return a in v


def bubble_sort(v: list) -> list:
    """ Sort the elements of v in ascending order
    >>> bubble_sort([4,2,5,1,3])
    [1, 2, 3, 4, 5]
    >>> bubble_sort([1,2,4,8,3,5,6,7,9,0])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
	Include these tokens in the code: 
		1.  Create a new list that is a copy of v
		2.  Use a while loop and an if statement to check each element in the list
		