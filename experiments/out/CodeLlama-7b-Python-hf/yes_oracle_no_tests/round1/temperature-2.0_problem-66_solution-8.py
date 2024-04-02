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
    
	Include these tokens in the code: return sum ([ ord ( ch ) for ch in
	"""
    # s = "abAB"
    sum = 0
    for ch in s:
        code = ord(ch)
        if code >= 65 and code <= 90:
            sum += code
    return sum


# print(digitSum(""))
# print(digitSum("abAB"))
# print(digitSum("abcCd"))
# print(digitSum("helloE"))
# print(digitSum("woArBld"))
# print(digitSum("aAaaaXa"))


def digitSum2(s):
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
    
	Include these tokens in the code: return sum ([ ord ( ch ) for ch in
	"""
    # s = "abAB"
    sum = 0
    for ch in s:
        code = ord(ch)
        if code >= 65 and code <= 90:
            sum += code
    return sum


# print(digitSum2(""))
# print(digitSum2("abAB"))
# print(digitSum2("abcCd"))
# print(digitSum2("helloE"))
# print(digitSum2("woArBld"))
# print(digitSum2("aAaaaXa"))


def digitSum3(s):
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld")