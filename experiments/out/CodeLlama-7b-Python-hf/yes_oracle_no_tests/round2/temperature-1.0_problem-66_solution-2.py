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
    
	Include these tokens in the code: return sum ([ ord ( ch )
	Do not include these tokens in the code: # First , I create a list
	"""
    sum = 0
    for ch in s:
        if ch.isupper():
            sum += ord(ch)
    return sum


def digitSum2(s):
    sum = 0
    for ch in s:
        if ch.isupper():
            sum += ord(ch)
    return sum


def digitSum3(s):
    return sum([ord(ch) for ch in s if ch.isupper()])


if __name__ == '__main__':
    print(digitSum(""))
    print(digitSum("abAB"))
    print(digitSum("abcCd"))
    print(digitSum("helloE"))
    print(digitSum("woArBld"))
    print(digitSum("aAaaaXa"))
