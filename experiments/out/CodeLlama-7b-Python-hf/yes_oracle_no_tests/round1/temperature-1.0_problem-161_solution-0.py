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

    ans = ""
    has_letter = False
    for char in s:
        if char.isalpha():
            if has_letter:
                ans+=char.swapcase()
            else:
                has_letter = True
                ans+=char.lower()
        else:
            ans+=char
            if (has_letter):
                break
    if (has_letter == False):
        ans = ans[::-1]
    print(ans)
    return ans

#solve("Bacon, let's eat Mcflast.")

#----------------------------------------------------------------------------------

def solve(s):
    """You are given a string s.
    reverse its order transforming it into an integer and return it. Return it back as a string.
    Examples
    reverse_int("1234") = "4321"
    reverse_int("123") = "321"
    
    Include these tokens in the code: ans , has _ number
    Do not include these tokens in the code: s
    """
    ans = ""
    has_number = False
    for char in s:
        if char.isdigit():
            if has_number:
                ans+=char
            else:
                has_number = True
                ans+=char
        else:
            if (has_number):
                break
    ans = ans[::-1]
    print(ans)
    return ans