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
    # s = 'abAB'
    sum = 0
    for ch in s:
        if ord(ch) > 64 and ord(ch) < 91:
            sum += ord(ch)
    return sum


# print(digitSum('abAB'))
# print(digitSum('abcCd'))
# print(digitSum('helloE'))
# print(digitSum('woArBld'))
# print(digitSum('aAaaaXa'))


def testDigitSum():
    assert digitSum('') == 0
    assert digitSum('abAB') == 131
    assert digitSum('abcCd') == 67
    assert digitSum('helloE') == 69
    assert digitSum('woArBld') == 131
    assert digitSum('aAaaaXa') == 153


if __name__ == '__main__':
    testDigitSum()
