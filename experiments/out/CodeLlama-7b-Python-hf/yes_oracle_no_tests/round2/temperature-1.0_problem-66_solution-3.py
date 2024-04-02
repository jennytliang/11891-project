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
    
	Do not include these tokens in the code: s = s . upper ()
	"""
    def toUpper(string):
        chars = ""
        for c in string:
            if c.isupper():
                chars += c
        return chars
    
    s = s.upper()
    sum = 0
    for c in s:
        d = ord(c)
        if d > 64 and d < 91:
            sum += d
    return sum

def checkDigit(s):
    """Task
    Write a function that takes a string and returns true if it is a digit, and false otherwise

    Examples:
        checkDigit("") => false
        checkDigit("a") => false
        checkDigit("1") => true
    """
    b = s.isdigit()
    return b

def checkDigit2(s):
    for c in s:
        if not c.isdigit():
            return False
                
    return True

def checkNumber(n):
    """Task
    The sum of the square roots of the digits is even.

    Examples:
        checkNumber(-1) => ""
        checkNumber(0) => "1: 0"
        checkNumber(1234) => "8: 3"
        checkNumber(35) => "6: 5"
    """
    strNum = str(n)
    numCheck = n
    sCheck = True
    index = 0
    s = ""
    while index < len(strNum) and sCheck == True:
        s = s + " " + str(numCheck) + ": " + str(int(math.sqrt(int(strNum[index]))))
        numCheck = numCheck - int(strNum[index]) ** 2
        if numCheck < 0:
            sCheck = False
        if numCheck == 0:
            return s
        index = index + 1
    return ""

def checkNumber2(n):
    """Task
    The sum of the square roots of the digits is even.

    Examples:
        checkNumber(-1) => ""
        checkNumber(0) => "1: 0"
       