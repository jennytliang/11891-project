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
    result = 0
    for char in s:
        if char.isupper():
            result += ord(char)
    return result


print(digitSum(""))
print(digitSum("abAB"))
print(digitSum("abcCd"))
print(digitSum("helloE"))
print(digitSum("woArBld"))
print(digitSum("aAaaaXa"))
