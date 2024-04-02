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

    ## Code is below
    if (a == b):
        return True
    else:
        if(len(a) == len(b)):
            return False
        else:
            x = len(a)
            newa = a[0:int(x/2) -1]
            x = len(newa)
            if(newa == a[b:x + b]):
                return True
            else:
                for i in range(1,int(x/2)):
                    print(i)
                    if( newa == a[ b:x + b] == a[ x - i:x] == a[ x - i:x + b]  ):
                        return True
    return False


def cycpattern_check_new(a , b):
        if (a == b):
            return True
        else:
            if(len(a) == len(b)):
                return False
            else:
                x = len(a)
                newa = a[0:int(x/2) -1]
                x = len(newa)
                if(newa == a[b:x + b]):
                    return True
                else:
                    for i in range(1,int(x/2)):
                        print(i)
                        if( newa == a[ b:x + b] == a[ x - i:x] == a[ x - i:x + b]  ):
                            return True
                    return False

cycpattern_check_new("aabbbc","abb")                