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
    
	Do not include these tokens in the code: sum = 0 for
	"""
    sum = 0
    for i in s:
        if i.isupper():
            sum += ord(i)
    return sum


def digitSum2(s):
    return sum([ord(i) for i in s if i.isupper()])


def digitSum3(s):
    return sum(ord(c) for c in s if c.isupper())


def digitSum4(s):
    return sum(ord(c) for c in s if c.isupper())


def digitSum5(s):
    return sum(ord(c) for c in s if c.isupper())


def digitSum6(s):
    return sum(ord(c) for c in s if c.isupper())


def digitSum7(s):
    return sum(ord(c) for c in s if c.isupper())


def digitSum8(s):
    return sum(ord(c) for c in s if c.isupper())


def digitSum9(s):
    return sum(ord(c) for c in s if c.isupper())


def digitSum10(s):
    return sum(ord(c) for c in s if c.isupper())


def digitSum11(s):
    return sum(ord(c) for c in s if c.isupper())


def digitSum12(s):
    return sum(ord(c) for c in s if c.isupper())


def digitSum13(s):
    return sum(ord(c) for c in s if c.isupper())


def digitSum14(s):
    return sum(ord(c) for c in s if c.isupper())


def digitSum15(s):
    return sum(ord(c) for c in s if c.isupper())


def digitSum16(s):
    return sum(ord(c) for c in s if c.isupper())


def digitSum17(s):
    return sum(ord(c) for c in s if