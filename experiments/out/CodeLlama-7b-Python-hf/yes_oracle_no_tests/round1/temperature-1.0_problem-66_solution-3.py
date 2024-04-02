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
    s = s.upper()
    sum_ascii = sum(map(lambda x: ord(x), list(filter(lambda y: y.isupper(), s))))
    return sum_ascii


def digitSum_solution(s):
    """Alternative."""
    return sum([ord(c) for c in s.upper() if c.isupper()])


print(digitSum("123A456b"))
print(digitSum_solution("123A456b"))
print(digitSum("abcd"))
print(digitSum_solution("abcd"))
print(digitSum("a"))
print(digitSum_solution("a"))
print(digitSum(""))
print(digitSum_solution(""))
print(digitSum("HeLloB"))
print(digitSum_solution("HeLloB"))
