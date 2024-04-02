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
    
	Include these tokens in the code: ans ,
	"""
    ans = ""
    for x in s:
        if x.isalpha():
            ans += x.swapcase()
        else:
            ans += x
    if ans == "":
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
    
	Include these tokens in the code: ans ,
	"""
    ans = ""
    for x in s:
        if x.isalpha():
            ans += x.swapcase()
        else:
            ans += x
    return ans if ans else s[::-1]


if __name__ == '__main__':
    s = '1234'
    print(solve(s))
    print(solve2(s))
