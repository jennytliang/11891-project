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
    
	Include these tokens in the code: ans , has _ letter
	Do not include these tokens in the code: s
	"""
    #code here
    ans = ""
    has_letter = False
    for c in s:
        if c.isalpha():
            ans = ans + c.swapcase()
            has_letter = True
        else:
            ans = ans + c
    if not has_letter:
        ans = ans[::-1]
    return ans


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
        for line in lines:
            print(solve(line.strip()))
