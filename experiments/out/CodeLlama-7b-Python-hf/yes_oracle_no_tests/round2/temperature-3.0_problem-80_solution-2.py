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
    
	Include these tokens in the code: len
	Do not include these tokens in the code: 0 ,
	"""

    if len(s) < 3:
        return False
    foos = s[0:3]
    if len(foos) != len(set(foos)):
        return False
    if s[-3:] == foos:
        return is_happy(s[:-3])
    else:
        return is_happy(s[1:])


def is_happy_recursive(s):
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
    
	Include these tokens in the code: len
	Do not include these tokens in the code: 0 ,
	"""

    if len(s) < 3:
        return False
    foos = s[0:3]
    if len(foos) != len(set(foos)):
        return False
    if s[-3:] == foos:
        return is_happy_recursive(s[:-3])
    else:
        return is_happy_recursive(s[1:])


if __name__ == "__main__":
    print(is_happy("abc"))
    print(is_happy("abcd"))
    print(is_happy("adb"))
    print(is_happy("aabb"))
    print(is_happy("xyy"))
    print(is_happy_recursive("abc"))
    print(is_happy_recursive("abcd"))
    print(is_happy_recursive("adb"))
    print(is_happy_recursive("aabb"))
    print(is_happy_recursive("xyy"))
