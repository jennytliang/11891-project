def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    
	Include these tokens in the code:  if a == b :
	Do not include these tokens in the code: len ( ) < len (
	"""

    def rotate(s):
        return s[1:] + s[0]

    def cyclic_pattern(a, b):
        if a == b:
            return False
        rotated_b = rotate(b)
        return rotated_b in a

    return cyclic_pattern(a, b)


def cycpattern_check2(a, b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    def rotate(s):
        return s[1:] + s[0]

    def cyclic_pattern(a, b):
        if a == b:
            return False
        rotated_b = rotate(b)
        return rotated_b in a

    return cyclic_pattern(a, b)


def cycpattern_check3(a, b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if a == b:
        return False
    rotated_b = rotate(b)
    return rotated_b in a


def rotate(s):
    return s[1:] + s[0]


