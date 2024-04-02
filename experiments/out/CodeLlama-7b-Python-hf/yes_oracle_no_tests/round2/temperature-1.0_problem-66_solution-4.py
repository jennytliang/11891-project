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

    # code here
    total = 0
    for i in range(len(s)):
        if s[i].isupper():
            total += ord(s[i])
    return total


# print(digitSum(""))
# print(digitSum("abAB"))
# print(digitSum("abcCd"))
# print(digitSum("helloE"))
# print(digitSum("woArBld"))
# print(digitSum("aAaaaXa"))






















































































































