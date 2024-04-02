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
    l = len(a)
    for i in range(l):
        if a[i:l] + a[0:i] == b:
            return True
    return False


def cycpattern_check1(a, b):
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
    l = len(a)
    return b in a * l or b in a[1:] * l


if __name__ == "__main__":
    print(cycpattern_check("abcd", "abd"))
    print(cycpattern_check("hello", "ell"))
    print(cycpattern_check("whassup", "psus"))
    print(cycpattern_check("abab", "baa"))
    print(cycpattern_check("efef", "eeff"))
    print(cycpattern_check("himenss", "simen"))
    print(cycpattern_check("abcabc", "abc"))
    print(cycpattern_check("abcabc", "cabc"))
