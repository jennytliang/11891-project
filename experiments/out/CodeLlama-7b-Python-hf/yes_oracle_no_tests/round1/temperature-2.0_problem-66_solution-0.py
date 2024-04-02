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
    
	Include these tokens in the code: ch
	Do not include these tokens in the code: x
	"""


    return sum([ord(ch) for ch in s if ch.isupper()])


# 2nd way
def digitSum_2(s):
    return sum([ord(ch) for ch in s if ch.isupper()])



# 3rd way
def digitSum_3(s):
    return sum(ord(ch) for ch in s if ch.isupper())


# 4th way
def digitSum_4(s):
    return sum(ord(ch) for ch in s if ch.isupper())



# 5th way
def digitSum_5(s):
    return sum(ord(ch) for ch in s if ch.isupper())



# 6th way
def digitSum_6(s):
    return sum(ord(ch) for ch in s if ch.isupper())



# 7th way
def digitSum_7(s):
    return sum(ord(ch) for ch in s if ch.isupper())



# 8th way
def digitSum_8(s):
    return sum(ord(ch) for ch in s if ch.isupper())

































































































































































































































