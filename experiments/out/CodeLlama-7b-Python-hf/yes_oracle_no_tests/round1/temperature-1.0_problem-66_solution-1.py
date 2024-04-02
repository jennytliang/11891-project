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
    res = []
    for s1 in s:
        if s1 == s1.upper():
            res.append(ord(s1)) # ord(s1)
    
    sum = 0
    for r in res:
        sum = sum + r

    return sum

if __name__ == "__main__":
    print(digitSum("abAB"))

    digits=["abAB", "abcCd", "helloE", "woArBld", "aAaaaXa"]
    # print(digitSum(digits[0]))
    # print(type(digits[1]))
    print(digitSum(list(digits)))

    def sum_digits(string):
        if len(string) == 0:
            return 0

        digits = "0123456789"
        return int(string[0]) + sum_digits(string[1:]) if string[0] in digits else sum_digits(string[1:])
