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
    if len(ans) > 0:
        if ans[0] == " ":
            ans = "_" + ans[1:]
        ans = ans.replace("  ", "-")
        ans = ans.replace(" ", "_")
    return ans


print(fix_spaces("Example"))
print(fix_spaces("Example 1"))
print(fix_spaces(" Example 2"))
print(fix_spaces(" Example   3"))
print(fix_spaces("  Example   4"))
print(fix_spaces("  Example   5  "))
print(fix_spaces("  Example   6   "))
print(fix_spaces("  Example   7    "))
print(fix_spaces("  Example   8     "))
print(fix_spaces("  Example   9      "))
print(fix_spaces("  Example   10       "))
print(fix_spaces("  Example   11        "))
print(fix_spaces("  Example   12         "))
print(fix_spaces("  Example   13          "))
print(fix_spaces("  Example   14           "))
print(fix_spaces("  Example   15            "))
print(fix_spaces("  Example   16             "))
print(fix_spaces("  Example   17              "))
print(fix_spaces("  Example   18               "))
print(fix_spaces("  Example   19                "))
print(fix_spaces("  Example   20                 "))
print(fix_spaces("  Example   21                  "))
print(fix_spaces("  Example   22                   "))
print(fix_spaces("  Example   23                    "))
print(fix_spaces("  Example   24                     "))
print(fix_spaces("  Example   25                      "))
print(fix_spaces("  Example   26                       "))
print(fix_spaces("  Example   27                        "))
print(fix_spaces("  Example   28                         "))
print(fix_spaces("  Example   29                          "))
print