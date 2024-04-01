def solve(s):
    """You are given a string s.
    if s[i] is a letter, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains no letters, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "4321"
    solve("ab") = "AB"
    solve("#a@C") = "#A@c"
    """
    letters = s.isalpha()  
    up = s.isupper()       
    reversal = False       
    res = ''                
    # check for letters
    for s_ in s:                           
        if letters:         
            if (up and (s_>='a' and s_<='z') ) or \
                (not(up) and  (s_>='A' and s_<='Z')):    
                    reversal = not(reversal)       
                    s_ =  s_.upper() if s_>='a'and s_<='z' else s_.lower() 
            else:          
               pass                
        else:                              
            res = s                    
            return res                                   
    return s if reversal else ''.join(list(reversed(res))) if len(res)>0 else res
   
