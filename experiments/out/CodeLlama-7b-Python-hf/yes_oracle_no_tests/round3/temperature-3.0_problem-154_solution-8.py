def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    
	Include these tokens in the code: True
	Do not include these tokens in the code: Tru
	"""


    if a == b:
        
        return True
    
    if len(a) != len(b):
        
        return False

    a_list = list(a)

    b_list = list(b)
    b_list_rotated = b_list.copy()

    b_list_rotated = b_list_rotated[1:] + b_list_rotated[:1]


    if b_list in a_list:
        return True

    if b_list_rotated in a_list:
        return True
    
    return False

