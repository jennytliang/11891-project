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
    ans = ''
    has_letter = False
    for char in s:
        if char.isalpha():
            has_letter = True
            if char.islower():
                ans += char.upper()
            else:
                ans += char.lower()
        else:
            ans += char
    if not has_letter:
        return ans[::-1]
    return ans


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
    for line in lines:
        s = line.split()[0]
        print(solve(s))