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
    has_letter = False
    for i in s:
        if i.isalpha():
            has_letter = True
            break
    ans = ""
    if has_letter == False:
        return s[::-1]
    for i in s:
        if i.isalpha():
            if i.islower():
                ans += i.upper()
            else:
                ans += i.lower()
        else:
            ans += i
    return ans

if __name__ == '__main__':
    with open('input.txt') as f:
        s = f.readline().strip()

    print(solve(s))