def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if a.isspace() or a.replace(" ", "")=='' or b.isspace(): return False
         
    else:
            
        l1=(a + a).replace( b , "") 
        n=a.find( b ) 
        c1=a[0:n]
        d=l1.count(b)
        
        bb=(b +b ).count( b ) 
            
        if d==0:
            return False        
        else:
            if (n==len(a)) or (n==0): return True
            elif (c1.count( c1)!=bb): return False 
            elif (n+2*(len(b) )<= len( a )): return cycpattern_check(c1,b) 


"""if a in (a + a): return True
elif (a in (b)): return True
        else : return False"""