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
	Do not include these tokens in the code: # code goes here new
	"""
    #code
    ans = ''
    has = False
    for char in s:
        if char.isalpha():
            ans += char.swapcase()
            has = True
        else:
            ans += char
    if not has: ans = s[::-1]
    return ans

print(solve("1234"))
print(solve("ab"))
print(solve("#a@C"))
print(solve("AaBbCc"))
