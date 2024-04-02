def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    
	Include these tokens in the code: if b == " ":
	Do not include these tokens in the code: a _ list = list ( a )
	"""

    if a == b:
        return Tru

    if a and b:
        a_list = list(a)
        if len(a_list) >= len(b):
            len_b = [index+1 for index,i in enumerate(a_list) if a_list[index + len(b)] == b[index]]
            if len(len_b) == len(b):
                if len(len_b) ==1:
                    return True
                elif max(len_b) == len(a_list):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False




