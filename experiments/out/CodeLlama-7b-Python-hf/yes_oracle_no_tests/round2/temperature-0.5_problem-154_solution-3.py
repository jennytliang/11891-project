def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    
	Do not include these tokens in the code: if len ( a ) <
	"""
    if len(b) > len(a):
        return False
    for i in range(len(a) - len(b) + 1):
        if a[i:i + len(b)] == b:
            return True
    return False


print(cycpattern_check('abc', 'cba'))
print(cycpattern_check('abc', 'ab'))
print(cycpattern_check('abc', 'bc'))
