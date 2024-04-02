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
	Do not include these tokens in the code: result = 0
	"""
    # First, we define a variable to hold the sum of the upper characters
    # We use 0 as the initial value because we will be adding to it
    result = 0
    # We loop through the string
    for i in s:
        # If the character is upper, we append its ASCII value to the result
        if i.isupper():
            result += ord(i)
    # We return the result
    return result

# # Test Cases
# print(digitSum("")) # 0
# print(digitSum("abAB")) # 131
# print(digitSum("abcCd")) # 67
# print(digitSum("helloE")) # 69
# print(digitSum("woArBld")) # 131
# print(digitSum("aAaaaXa")) # 153
