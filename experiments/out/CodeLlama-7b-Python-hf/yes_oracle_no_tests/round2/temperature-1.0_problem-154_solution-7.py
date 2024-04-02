def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    
	Include these tokens in the code: if a == b :
	"""
    
    return (a+a).find(b) != a+1

print([cycpattern_check("abcd","abd"),cycpattern_check("hello","ell"),cycpattern_check("whassup","psus"),cycpattern_check("abab","baa"),cycpattern_check("efef","eeff"),cycpattern_check("himenss","simen"),])