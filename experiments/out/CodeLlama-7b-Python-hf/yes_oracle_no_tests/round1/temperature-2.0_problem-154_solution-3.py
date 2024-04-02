def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    
	Include these tokens in the code: if a == b : return True
	"""
    if a == b:
        return True
    a_len = len(a)
    b_len = len(b)
    for i in range(a_len):
        if a[i:a_len] + a[0:i] == b:
            return True
    return False


def cycpattern_check_v2(a, b):
    if a == b:
        return True
    a_len = len(a)
    b_len = len(b)
    for i in range(a_len):
        if a[i:] + a[:i] == b:
            return True
    return False


print(cycpattern_check("abcd", "abd"))
print(cycpattern_check("hello", "ell"))
print(cycpattern_check("whassup", "psus"))
print(cycpattern_check("abab", "baa"))
print(cycpattern_check("efef", "eeff"))
print(cycpattern_check("himenss", "simen"))

print(cycpattern_check_v2("abcd", "abd"))
print(cycpattern_check_v2("hello", "ell"))
print(cycpattern_check_v2("whassup", "psus"))
print(cycpattern_check_v2("abab", "baa"))
print(cycpattern_check_v2("efef", "eeff"))
print(cycpattern_check_v2("himenss", "simen"))
