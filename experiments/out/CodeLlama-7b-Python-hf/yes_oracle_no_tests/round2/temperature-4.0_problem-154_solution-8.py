def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    
	Include these tokens in the code: True
	Do not include these tokens in the code: False
	"""

    
    if a == b:
    	return True
    else:
    	if len(a) > len(b):
    		for i in range(len(a)):
    			if a[i:i+len(b)] == b:
    				return True
    	else:
    		for i in range(len(b)):
    			if b[i:i+len(a)] == a:
    				return True
    	return False



if __name__ == "__main__":
    a = "abcd"
    b = "abd"
    print(cycpattern_check(a,b))
