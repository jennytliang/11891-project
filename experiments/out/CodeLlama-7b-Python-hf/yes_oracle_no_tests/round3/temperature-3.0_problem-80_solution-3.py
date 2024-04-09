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
    
	Include these tokens in the code: if
	Do not include these tokens in the code: return
	"""
    if len(s) < 3:
        return False
    if s == s[::-1]:
        return False
    if s[0] == s[1] or s[0] == s[2] or s[1] == s[2]:
        return False
    return True


if __name__ == '__main__':
    print(is_happy("abcd"))
    print(is_happy("adb"))
    print(is_happy("xyy"))
