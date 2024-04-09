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
    
	Include these tokens in the code: ([
	Do not include these tokens in the code: (
	"""


    retu = 0
    for i in s:
        if ord(i) > 64 and ord(i) < 91:
            retu += ord(i)
    return retu


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
    
	Include these tokens in the code: ([
	Do not include these tokens in the code: (
	"""


    retu = 0
    for i in s:
        if i.isupper():
            retu += ord(i)
    return retu


def digitSum3(s):
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
    
	Include these tokens in the code: ([
	Do not include these tokens in the code: (
	"""


    return sum(ord(i) for i in s if i.isupper())


print(digitSum3("aAaaaXa"))
