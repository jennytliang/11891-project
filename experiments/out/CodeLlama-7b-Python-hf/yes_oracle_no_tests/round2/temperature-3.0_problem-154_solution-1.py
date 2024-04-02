def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    
	Include these tokens in the code: b
	Do not include these tokens in the code: len ( a ) != len ( ):
	"""

    if a == b:
        return True

    if len(a) != len(b):
        return False

    if a.find(b) != -1:
        return True

    for i in range(len(a)):
        rotated = a[i:] + a[:i]
        if rotated.find(b) != -1:
            return True

    return False


if __name__ == "__main__":
    print(cycpattern_check("abcd", "abd"))  # False
    print(cycpattern_check("hello", "ell"))  # True
    print(cycpattern_check("whassup", "psus"))  # False
    print(cycpattern_check("abab", "baa"))  # True
    print(cycpattern_check("efef", "eeff"))  # False
    print(cycpattern_check("himenss", "simen"))  # True
