def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    
	Include these tokens in the code: if len ( list ( filter ( lambda ch :
	"""
    pass


def is_palindrome(string):
    """Create a function which takes a string and returns 'Yes' if the string is a palindrome,
    and 'No' otherwise.
    A string is considered to be a palindrome if it reads the same forwards and backwards,
    ignoring case and spaces.
    Examples:
    is_palindrome("Level") # => 'Yes'
    is_palindrome("Level. ") # => 'No' (the string should ignore the dot and the space)
    is_palindrome("Level.Not") # => 'No' (the string should ignore the dot and the space)
    """
    pass


def is_prime(number):
    """Create a function which takes an integer and returns 'Yes' if the integer is a prime,
    and 'No' otherwise.
    An integer is considered to be a prime if it is greater than 1, and it is divisible only
    by 1 and itself.
    Examples:
    is_prime(2) # => 'Yes'
    is_prime(15) # => 'No'
    is_prime(11) # => 'Yes'
    """
    pass


def is_triangle(a, b, c):
    """Create a function which takes three integers a, b, and c, and returns 'Yes' if the
    three integers form a triangle, and 'No' otherwise.
    An integer a, b, and c form a triangle if and only if the following condition is met:
    a + b > c, and b + c > a, and c + a > b
    Examples:
    is_triangle(1, 2, 2) # => 'Yes'
    is_triangle(1, 2, 3) # => 'No'
    is_triangle(5, 1, 1) # => 'No'
    """
    pass


def is_vowel(letter):
    """Create a function which takes a single letter and returns 'Yes' if the letter is a
    vowel, and 'No' otherwise.
    A letter is considered to be a vowel if