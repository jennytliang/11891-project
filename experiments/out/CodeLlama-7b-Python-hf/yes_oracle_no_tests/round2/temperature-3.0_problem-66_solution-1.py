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
	Do not include these tokens in the code: # First , we create a variable
	"""
    return sum([ord(i) for i in s if i.isupper()])

    # return sum([ord(i) for i in s if ord(i) >= 65 and ord(i) <= 90])

    # return sum([ord(i) for i in s if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'])

    # s = list(s)
    # sum = 0
    # for i in range(len(s)):
    #     if s[i].isupper():
    #         sum += ord(s[i])
    # return sum


if __name__ == '__main__':
    print("Example:")
    print(digitSum('abAB'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert digitSum('abAB') == 131
    assert digitSum('abcCd') == 67
    assert digitSum('helloE') == 69
    assert digitSum('woArBld') == 131
    assert digitSum('aAaaaXa') == 153
    assert digitSum('') == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")