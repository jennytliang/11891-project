def digitSum(s):
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    
	Include these tokens in the code: return
	Do not include these tokens in the code: # First , we define a variable
	"""
    # First , we define a variable to sum the digits
    sum = 0
    # For each character in the string
    for char in s:
        # If the character is upper case
        if char.isupper():
            # We add its ASCII code to the sum
            sum += ord(char)
    # We return the sum
    return sum


# E. Given 2 strings, a and b, return a string of the form short+long+short,
# with the shorter string on the outside and the longer string on the inside.
# The result should be a new string and not just concatenation.
def combo_string(a, b):
    """Task
    Write a function that takes two strings as input and returns a string of the form short+long+short,
    with the shorter string on the outside and the longer string on the inside.
    The result should be a new string and not just concatenation.

    Examples:
        combo_string("Hello", "hi") => "hiHellohi"
        combo_string("hi", "Hello") => "hiHellohi"
        combo_string("aaa", "b") => "baaab"
        combo_string("aaa", "aa") => "aaaaaa"
    
	Include these tokens in the code: return
	Do not include these tokens in the code: # First , we define a variable
	"""
    # First , we define a variable to store the result
    result = ""
    # If the first string is shorter than the second
    if len(a) < len(b):
        # We add the shorter string to the result
        result += a
        # Then we add the longer string to the result
        result += b
        # Finally, we add the shorter string to the result
        result += a
    # If the first string is longer than the second
    elif len(a) > len(b):
        # We add the longer string to the result
        result += b
        # Then we add the shorter string to the result
        result += a
        # Finally, we add the longer string to the result
        result += b
    # If both strings are the