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
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if a[i:] + a[:i] == b:
            return True
    return False


def cycpattern_check_2(a, b):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check_2("abcd","abd") => False
    cycpattern_check_2("hello","ell") => True
    cycpattern_check_2("whassup","psus") => False
    cycpattern_check_2("abab","baa") => True
    cycpattern_check_2("efef","eeff") => False
    cycpattern_check_2("himenss","simen") => True


    """
    if a == b:
        return True
    if len(a) != len(b):
        return False
    a_set = set(a)
    b_set = set(b)
    if len(a_set) != len(b_set):
        return False
    for i in range(len(a)):
        if a[i:] + a[:i] == b:
            return True
    return False


def cycpattern_check_3(a, b):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check_3("abcd","abd") => False
    cycpattern_check_3("hello","ell") => True
    cycpattern_check_3("whassup","psus") => False
    cycpattern_check_3("abab","baa") => True
    cycpattern_check_3("efef","eeff") => False
    cycpattern_check_3("himenss","simen") => True


    """
    if a == b:
        return True
   