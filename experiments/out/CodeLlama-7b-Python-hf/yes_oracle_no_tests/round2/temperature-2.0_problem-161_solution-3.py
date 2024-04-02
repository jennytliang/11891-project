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
    # code goes here
    ans = ""
    has_letter = False
    for char in s:
        if char.isalpha():
            if char.islower():
                ans += char.upper()
            else:
                ans += char.lower()
            has_letter = True
        else:
            ans += char
    if not has_letter:
        ans = ans[::-1]
    return ans


# keep this function call here 
print(solve(input()))
