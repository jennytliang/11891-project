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
    
	Include these tokens in the code: ans , has _ letter = "", False
	"""
    s = list(s)
    ans = ""
    has_letter = False
    for i in range(len(s)):
        if s[i].isalpha():
            has_letter = True
            if s[i].isupper():
                s[i] = s[i].lower()
            else:
                s[i] = s[i].upper()
        ans += s[i]
    if not has_letter:
        return s[::-1]
    return ans


def solve2(s):
    """You are given a string s.
    if s[i] is a letter, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains no letters, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "4321"
    solve("ab") = "AB"
    solve("#a@C") = "#A@c"
    
	Include these tokens in the code: ans , has _ letter = "", False
	"""
    s = list(s)
    ans = ""
    has_letter = False
    for i in range(len(s)):
        if s[i].isalpha():
            has_letter = True
            if s[i].isupper():
                s[i] = s[i].lower()
            else:
                s[i] = s[i].upper()
        ans += s[i]
    if not has_letter:
        return s[::-1]
    return ans


def solve3(s):
    """You are given a string s.
    if s[i] is a letter, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains no letters, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "4321"
    solve("ab") = "AB"
    solve("#a@C") = "#A@c"
    
	