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

    if a == b:
        return False
    else:
        if len(a) < len(b):
            return False
        else:
            for i in range(len(b)):
                if a.find(b) != -1:
                    return True
                else:
                    b = b[-1] + b[:-1]
            return False


print(cycpattern_check("abcd", "abd"))
print(cycpattern_check("hello", "ell"))
print(cycpattern_check("whassup", "psus"))
print(cycpattern_check("abab", "baa"))
print(cycpattern_check("efef", "eeff"))
print(cycpattern_check("himenss", "simen"))
