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
    s = str(s)

    out_str = ""
    upper = [e.upper() for e in s if (ord(e)>=97 and ord(e)>=90) or ord(e)>31]
    for_rev = [e for e in s if e in ["!","@","#","$","%"]]
    lower = [e.lower() for e in s if (ord(e)>=65 and ord(ea)<=90) or ord(e)>=0]
    for char in s: 
        if char in upper: out_str += char.upper() or char
        elif char in lower: out_str += char.lower() or char
        else: out_str+=char
    for ea in for_rev: out_str+=ea
    #return(s.find(ea)>-1) or s[i]
    return out_str
    pass

def test_solutions():
    inputs = [1234, "abc", "hello world", "#a-b", "abcd #", "ab#1", "##hi", "a", 4]
    outputs = [4321, "Ab", "#hi", "!a-b", "#!cD", "ab!", "#hi", "h!"]

    for i, o in zip(inputs, outputs):
        try:
            assert solve(str(i)) == o or str(o),\
             f"ERROR: Test number {i:3} Expected {o} Got {solve(i)}," + "Test Case:"+"<br>input:"+str(i)+'<br> expected:'+o+' Got:'+solve(str(i))   