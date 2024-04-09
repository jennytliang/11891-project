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
    
	Do not include these tokens in the code: # %% s = input ()
	"""
    if not s.isalpha():
        return s[::-1]
    else:
        return s.swapcase()


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
    
	Do not include these tokens in the code: # %% s = input ()
	"""
    return s.swapcase() if s.isalpha() else s[::-1]


# TESTS
assert solve("1234") == "4321"
assert solve("ab") == "AB"
assert solve("#a@C") == "#A@c"
assert solve("AbC") == "bcA"
assert solve("AbC123") == "cBA321"
assert solve("Ab3C123") == "3cB1A23"
assert solve("Ab3C123#") == "#3cB1A23#"
