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
    # s = input("")
    # s = "abAB"
    # s = "abcCd"
    # s = "helloE"
    # s = "woArBld"
    # s = "aAaaaXa"
    # s = "123456"
    # s = "123456789"
    # s = "1234567890"
    # s = "aBcDeF"
    # s = "aBcDeF1234567890"
    # s = "aBcDeF1234567890"

    sum = 0

    for ch in s:
        if ch.isupper():
            sum += ord(ch)

    return sum


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
    # s = input("")
    # s = "abAB"
    # s = "abcCd"
    # s = "helloE"
    # s = "woArBld"
    # s = "aAaaaXa"
    # s = "123456"
    # s = "123456789"
    # s = "1234567890"
    # s = "aBcDeF"
    # s = "aBcDeF1234567890"
    # s = "aBcDeF12