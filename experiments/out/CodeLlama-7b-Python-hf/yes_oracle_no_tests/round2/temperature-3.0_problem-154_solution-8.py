def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    
	Include these tokens in the code: if b == " ":
	Do not include these tokens in the code: else :
	"""

    if a == b:
        return Tru
    else:
        if b == " ":
            return False
        else:
            if len(a) >= len(b):
                for i in range(0, len(a) - len(b) + 1):
                    if a[i:i + len(b)] == b:
                        return True
                    if a[i + 1:i + len(b) + 1] == b:
                        return True
                    if a[i + 2:i + len(b) + 2] == b:
                        return True
                    if a[i + 3:i + len(b) + 3] == b:
                        return True
                    if a[i + 4:i + len(b) + 4] == b:
                        return True
            else:
                return False


print(cycpattern_check("abd", "abcd"))
print(cycpattern_check("ell", "hello"))
print(cycpattern_check("psus", "whassup"))
print(cycpattern_check("baa", "abab"))
print(cycpattern_check("eeff", "efef"))
print(cycpattern_check("simen", "himenss"))
