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
    sum = 0
    for i in s:
        if i.isupper():
            sum += ord(i)
    return sum


def digitSum2(s):
    return sum(ord(c) for c in s if c.isupper())


print(digitSum2(""))
print(digitSum2("abAB"))
print(digitSum2("abcCd"))
print(digitSum2("helloE"))
print(digitSum2("woArBld"))
print(digitSum2("aAaaaXa"))

