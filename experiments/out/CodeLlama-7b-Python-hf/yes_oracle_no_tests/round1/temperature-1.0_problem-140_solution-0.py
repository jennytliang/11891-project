def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    
	Include these tokens in the code: ans = text for i in range (
	"""

    # ans = text 
    # for i in range(len(text)):
    #     if text[i] == ' ':
    #         ans += '_'
    #         if (text[i+1] == ' ')



    ans = ''

    for i in range(len(text)):
        if not text[i] == ' ':
            ans += text[i]
        else:
            ans += '-'

    return ans

print('passed' if (fix_spaces('Example') == 'Example') else 'failed on "Example"')
print('passed' if (fix_spaces('Example 1') == 'Example_1') else 'failed on "Example 1"')
print('passed' if (fix_spaces(' Example 2') == '_Example_2') else 'passed on " Example 2"')
print('passed' if (fix_spaces(' Example   3') == '_Example-3') else 'failed on " Example   3"')