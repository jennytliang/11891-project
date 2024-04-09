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
	Do not include these tokens in the code: result = 0
	"""
    sum = 0
    for ch in s:
        if ch.isupper():
            sum += ord(ch)
    return sum
    # return sum([ord(ch) for ch in s if ch.isupper()])


def main():
    print(digitSum("")) # => 0
    print(digitSum("abAB")) # => 131
    print(digitSum("abcCd")) # => 67
    print(digitSum("helloE")) # => 69
    print(digitSum("woArBld")) # => 131
    print(digitSum("aAaaaXa")) # => 153


if __name__ == '__main__':
    main()
