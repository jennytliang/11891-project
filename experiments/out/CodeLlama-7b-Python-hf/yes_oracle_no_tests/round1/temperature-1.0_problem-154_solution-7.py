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
    # a = a.lower()
    # b = b.lower()
    # if a == b:
    #     return True
    # if len(a) != len(b):
    #     return False
    # for i in range(len(a)):
    #     if a[i:] + a[:i] == b:
    #         return True
    # return False
    # return len(set(a+a[:-1]))==len(set(b+b[:-1]))
    return len(set(a+a[:-1]))==len(set(b+b[:-1]))
