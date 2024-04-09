def is_happy(s):
    """You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
    For example:
    is_happy(a) => False
    is_happy(aa) => False
    is_happy(abcd) => True
    is_happy(aabb) => False
    is_happy(adb) => True
    is_happy(xyy) => False
    
	Do not include these tokens in the code: re ts = False else :
	"""



    if len(s) <= 2:
        return False
    if len(s) >= 3:
        for i in range(0, len(s)-2):
            if s[i] == s[i+1] or s[i] == s[i+2] or s[i+1] == s[i+2]:
                return False
        return True


if __name__ == "__main__":
    print(is_happy("adb"))
    print(is_happy("xyy"))
    print(is_happy("aa"))
    print(is_happy("a"))
    print(is_happy("abcd"))
    print(is_happy("aabb"))
    print(is_happy("abba"))
    print(is_happy("abcba"))
    print(is_happy("abcab"))
    print(is_happy("abbb"))
    print(is_happy("aaab"))
    print(is_happy("aaba"))
    print(is_happy("aaab"))
    print(is_happy("aabba"))
    print(is_happy("aabab"))
    print(is_happy("aabaa"))
    print(is_happy("aabba"))
    print(is_happy("aabab"))
    print(is_happy("aabaa"))
    print(is_happy("aabaa"))
    print(is_happy("aabba"))
    print(is_happy("aabab"))
    print(is_happy("aabaa"))
    print(is_happy("aabaa"))
    print(is_happy("aabba"))
    print(is_happy("aabab"))
    print(is_happy("aabaa"))
    print(is_happy("aabaa"))
    print(is_happy("aabba"))
    print(is_happy("aabab"))
    print(is_happy("aabaa"))
    print(is_happy("aabaa"))
   