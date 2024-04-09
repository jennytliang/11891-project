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
	Do not include these tokens in the code: str
	"""
    if not s.isalpha():
        return s[::-1]
    else:
        ans = ""
        for i in range (len(s)):
            if s[i].islower():
                ans += s[i].upper()
            else:
                ans += s[i].lower()
        return ans

if __name__ == '__main__':
    with open('./data.txt') as f:
        test_cases = f.readlines()
        for x in test_cases:
            input_x = x.split(";")[0]
            output_x = x.split(";")[1].strip("\n")
            result = solve(input_x)
            if result == output_x:
                print("Yeah!!!ud solved it")
            else:
                print("Oops, Try again!!!")
