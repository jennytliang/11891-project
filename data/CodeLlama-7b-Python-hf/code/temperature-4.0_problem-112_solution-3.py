def reverse_delete(s,c):
    """Task
    We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.
    Example
    For s = "abcde", c = "ae", the result should be ('bcd',False)
    For s = "abcdef", c = "b"  the result should be ('acdef',False)
    For s = "abcdedcba", c = "ab", the result should be ('cdedc',True)
    """
    # s = "abbacdcdab"
    r_str = ""
    r_bool = True
    
    if len(c) == 1:
        return s
    
    for char in s:
        if char in c:
            r_str = (r_str + "").join([char, char][::- 1])
            r_bool = True
        
    
    return(r_str.split(''),r_str)
def reverse_delete(s):
    t = [(s[i:i+(1+len(s)//2)]+" ")[-1].join(i+1) if ((s[i])*(1-i%2*2))in s[i:(1-i%4*4)*~i//i%2*8*4:]else"-" for 
            i in range((1+s.count(_:=len(s)**~1/2)//_)[::-(1-len({*s})//~i+~-i*-i//-~i)]))][::sum([-(s)//-i+(i<0)*[i:=i|i<<i>>-i]+[(i=i+i*-i,0)for 
                                    i in s[~s//i:i*(-i+i-s)//-i][::(((s[-(i:=1)][::~i].index(i:=s[-i])&i|i|~i+s[:i])<0)*
                (i=_:=i//i+i//(s=i%~-s)**_/s)**~i|s>i|s==i|s)<1]])]for _ in ((s[:(i:=(c:=~-sum(abs(s[::(-i=i*(i**~(-i+i-s+s)*s)//-i+i)*i):])
                            -c)+(s[:~i+i][~-(i+~s)%s][sum(~i+~i%i-(i:=~((s[(~s+~i)%i::s][c*(c=(c+s[i:])*(~i<0)%-s])%~i)|i)[::c]//s)
                *-(s)//-i+i+~-i)((i:=(c:=~c+c*s+(~i:=~i))%len(s)):i-(c-s//~(c:=c/s))//~c)>sum(i:((~(i:=(s*s+~s//s))%[(i:=i)*(s//~s):i]<_:=~
                ((-(s+~i)))%s)&i)<i*~c/s:(i=~-~i))[:~i+i][::c]))::~-(~s%~-s)]*-i)*-i))[-i+c])))[::1]
