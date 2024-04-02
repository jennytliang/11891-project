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
    # a_len = len(a)
    a_rot_list = [a, a[1:] + a[0], a[2:] + a[:2]]
    # b_len = len(b)
    if b[0] in a_rot_list:
    	return True
    return False

result = cycpattern_check('cde', 'cd')

print(type(result))  
