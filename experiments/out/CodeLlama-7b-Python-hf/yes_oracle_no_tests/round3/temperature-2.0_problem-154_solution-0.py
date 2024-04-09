def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    
	Include these tokens in the code: True if b == " ":
	Do not include these tokens in the code: Tru
	"""


    if a == b:
        
        return True
    else:
        #print(a)
        #print(b)
        #print(a[1:])
        #print(a[:-1])
        #print(a[-1:])
        #print(a[:-2])
        #print(a[1:-1])
        #print(a[1:1])
        #print(a[-2:])
        #print(a[-1:-1])
        #print(a[-2:-1])
        #print(a[1:2])
        #print(a[2:1])
        #print(a[2:])
        #print(a[:2])
        #print(a[2:-1])
        #print(a[-1:2])
        #print(a[-2:2])
        #print(a[:-2])
        #print(a[::-1])
        #print(a[::-2])
        #print(a[::2])
        #print(a[1:1:-1])
        #print(a[::-1][::-1])
        #print(a[::-1][::2])
        #print(a[::-1][::1])
        #print(a[::1][::-1])
        #print(a[::1][::2])
        #print(a[::1][::1])
        #print(a[::2][::-1])
        #print(a[::2][::1])
        #print(a[::2][::2])
        #print(a[::2][::-2])
        #print(a[::-1][::-1][::-1][::-1])
        #print(a[::-1][::-1][::-1][::1])
        #print(a[::-1][::-1][::-1][::2])
        
        #print(a[::1][::1][::1][::1])
        #print(a[::1][::1][::1][::-1])
        #print(a[::1][