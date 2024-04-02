def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    
	Include these tokens in the code: ans = text
	"""
    
    ans = text
    for i in range(0,len(ans)):
        if ans[i] != " ":
            continue
        if (i + 1) < len(ans) and ans[i + 1] == " ":
            ans = ans[0:i]+ "-" +ans[i+1:]
        ans = ans[0:i] + "_" + ans[i + 1:]
    return ans

import re
def fix_spaces1(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    
	Include these tokens in the code: ans = text
	"""
    
    ans = text
    for i in range(0,len(ans)):
        print("starting")
        if ans[i] != " ":
            continue
        pat = '  '
        ans = re.sub(pat, "-", ans)
        ans = re.sub(" ", "_", ans)
    return ans




if __name__ == '__main__':
    print(fix_spaces("Test 2   Test"))