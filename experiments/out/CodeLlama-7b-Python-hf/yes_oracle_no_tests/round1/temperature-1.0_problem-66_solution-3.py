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
    #code here
    sum = 0
    for i in range(len(s)):
        if (ord(s[i]) >= 65) and (ord(s[i]) <= 90):
            sum += ord(s[i])
    return sum

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert digitSum("") == 0, "Empty String"
    assert digitSum("abAB") == 131, "B and AB"
    assert digitSum("abcCd") == 67, "B and C"
    assert digitSum("helloE") == 69, "E"
    assert digitSum("woArBld") == 131, "woArBld"
    assert digitSum("aAaaaXa") == 153, "a, A and X"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
