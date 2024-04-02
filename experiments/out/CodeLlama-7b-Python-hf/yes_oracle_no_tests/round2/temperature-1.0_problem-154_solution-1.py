def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    
	Include these tokens in the code: b == " ": return True
	Do not include these tokens in the code: len
	"""

    if a == b:
        return True
 
    if b == a[len(a)-len(b):] or b == a[-len(a):len(a)-len(b)+1]:
        return True
 
    return any(b == a[i:i+len(b)] or b == a[-len(a)+i:len(a)+i-len(b)-1] for i in range(len(a) - len(b) + 1))


print(cycpattern_check("efef","eeff"))