def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    
	Include these tokens in the code: ),
	Do not include these tokens in the code: )): if text [ i ] == "
	"""

    ans = text
    for i in range(len(text)):
        if text[i] == " ":
            if text[i - 1] == " " and text[i + 1] == " ":
                ans = ans[:i + 1] + "-" + ans[i + 1:]
            else:
                ans = ans[:i] + "_" + ans[i + 1:]
    return ans


# TESTS
assert fix_spaces("Example") == "Example"
assert fix_spaces("Example 1") == "Example_1"
assert fix_spaces(" Example 2") == "_Example_2"
assert fix_spaces(" Example   3") == "_Example-3"
