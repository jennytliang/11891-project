def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    
	Do not include these tokens in the code: import math
	"""
    prime_length = 0
    for i in string:
        prime_length += 1
    if prime_length == 2 or prime_length == 3 or prime_length == 5 or prime_length == 7 or prime_length == 11 or prime_length == 13 or prime_length == 17 or prime_length == 19 or prime_length == 23 or prime_length == 29 or prime_length == 31 or prime_length == 37 or prime_length == 41 or prime_length == 43 or prime_length == 47 or prime_length == 53 or prime_length == 59 or prime_length == 61 or prime_length == 67 or prime_length == 71 or prime_length == 73 or prime_length == 79 or prime_length == 83 or prime_length == 89 or prime_length == 97 or prime_length == 101 or prime_length == 103 or prime_length == 107 or prime_length == 109 or prime_length == 113 or prime_length == 127 or prime_length == 131 or prime_length == 137 or prime_length == 139 or prime_length == 149 or prime_length == 151 or prime_length == 157 or prime_length == 163 or prime_length == 167 or prime_length == 173 or prime_length == 179 or prime_length == 181 or prime_length == 191 or prime_length == 193 or prime_length == 197 or prime_length == 199 or prime_length == 211 or prime_length == 223 or prime_length == 227 or prime_length == 229 or prime_length == 233 or prime_length == 239 or prime_length == 241 or prime_length == 251 or prime_length == 257 or prime_length == 263 or