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
    
	Do not include these tokens in the code: # code
	"""
    # your code here
    import re
    if re.search('[a-zA-Z]', s):
        s = s.swapcase()
    return s


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
    
	Do not include these tokens in the code: # code
	"""
    # your code here
    import re
    if re.search('[a-zA-Z]', s):
        s = ''.join(re.findall('[a-zA-Z]', s)).swapcase()
    return s


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
    
	Do not include these tokens in the code: # code
	"""
    # your code here
    import re
    if re.search('[a-zA-Z]', s):
        s = ''.join(re.findall('[a-zA-Z]', s)).swapcase()
    else:
        s = s[::-1]
    return s


def main():
    print(solve('1234'))
    print(solve('ab'))
    print(solve('#a@C'))

    print(solve2('1234'))
    print