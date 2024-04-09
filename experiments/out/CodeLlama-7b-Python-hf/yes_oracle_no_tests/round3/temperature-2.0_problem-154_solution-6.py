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
    
    if a == b[::-1]:
        
        return True
    
    a_list = list(a)
    b_list = list(b)
    
    b_list_rotated = b_list[::-1]
    
    for i in range(1,len(a)):
        
        if a_list[i:] == b_list:
            
            return True
        
        if a_list[:i] == b_list:
            
            return True
        
        if a_list[i:] == b_list_rotated:
            
            return True
        
        if a_list[:i] == b_list_rotated:
            
            return True
        
    return False


if __name__ == "__main__":
    a = "abcd"
    b = "abd"
    print(cycpattern_check(a,b))
    a = "hello"
    b = "ell"
    print(cycpattern_check(a,b))
    a = "whassup"
    b = "psus"
    print(cycpattern_check(a,b))
    a = "abab"
    b = "baa"
    print(cycpattern_check(a,b))
    a = "efef"
    b = "eeff"
    print(cycpattern_check(a,b))
    a = "himenss"
    b = "simen"
    print(cycpattern_check(a,b))
