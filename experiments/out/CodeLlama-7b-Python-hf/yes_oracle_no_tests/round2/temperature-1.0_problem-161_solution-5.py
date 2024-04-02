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
	Do not include these tokens in the code: string
	"""
    ## Code:
    letter = False        
    for c in s:
        if 'a'<=c<='z':
            letter = 'A'<=c<='Z'
            break
    return s[::-1] if letter==False else s.swapcase()


if __name__=="__main__":
    input = raw_input()
    result = solve(input)
    print result
    
"""Reference Code

def solve(s):
    # Your code here
    import string
    ans=""
    s=list(s)
    has_letter = False

    for c in s:
        if c in string.ascii_letters:
            has_letter = not has_letter
            break

    if has_letter:
        for c in s:
            if c in string.ascii_uppercase:
                ans+=c.lower()
            else:
                ans+=c.upper()
    else:
        ans = s[::-1]

    return ans

"""
