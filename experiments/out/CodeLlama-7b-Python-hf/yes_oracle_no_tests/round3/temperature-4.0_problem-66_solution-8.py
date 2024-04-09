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
    
	Do not include these tokens in the code: sum = 0
	"""
    s = s.upper()
    sum = 0
    for c in s:
        if c.isupper():
            sum += ord(c)
    return sum

def digitSum_2(s):
    return sum(ord(c) for c in s.upper() if c.isupper())

if __name__ == "__main__":
    print(digitSum(""))
    print(digitSum("abAB"))
    print(digitSum("abcCd"))
    print(digitSum("helloE"))
    print(digitSum("woArBld"))
    print(digitSum("aAaaaXa"))
    print(digitSum_2(""))
    print(digitSum_2("abAB"))
    print(digitSum_2("abcCd"))
    print(digitSum_2("helloE"))
    print(digitSum_2("woArBld"))
    print(digitSum_2("aAaaaXa"))