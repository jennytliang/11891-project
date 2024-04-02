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
 
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i:j] == b:
                return True
            else:
                return False
