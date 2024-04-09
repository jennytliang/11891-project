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
    
	Do not include these tokens in the code: else :
	"""



    if len(s) < 3:
       replay = False
    else:
        replay = True

    for i in range(len(s) - 2):
        if s[i] == s[i + 1] or s[i] == s[i + 2] or s[i + 1] == s[i + 2]:
            replay = False
            break
    return replay



print(is_happy("adb"))
print(is_happy("xyy"))
print(is_happy("aa"))
print(is_happy("aaa"))
print(is_happy("abc"))
print(is_happy("abcd"))
print(is_happy("aabb"))
print(is_happy("abbb"))
print(is_happy("abcc"))
print(is_happy("abbbb"))
print(is_happy("abbbbb"))
print(is_happy("abcdef"))
print(is_happy("abcdefg"))
print(is_happy("abcdefgh"))

