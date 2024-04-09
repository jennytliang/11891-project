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
    
	Include these tokens in the code: ans , has
	Do not include these tokens in the code: new
	"""
    ans = ""
    has = False
    for i in s:
        if i.isalpha():
            has = True
            if i.islower():
                ans += i.upper()
            else:
                ans += i.lower()
        else:
            ans += i
    if has == False:
        ans = s[::-1]
    return ans
