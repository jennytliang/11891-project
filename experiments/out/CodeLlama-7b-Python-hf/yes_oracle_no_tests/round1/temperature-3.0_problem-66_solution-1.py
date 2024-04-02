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
	"""
    # First, we create a variable to store the sum of the digits.
    total = 0
    
    # Then, we iterate through the string.
    for i in s:
        
        # We check if the current character is an uppercase letter.
        if i.isupper():
            
            # If it is, we add the digit's value to the sum.
            total += ord(i)
            
    # Finally, we return the sum.
    return total

print(digitSum(""))
print(digitSum("abAB"))
print(digitSum("abcCd"))
print(digitSum("helloE"))
print(digitSum("woArBld"))
print(digitSum("aAaaaXa"))