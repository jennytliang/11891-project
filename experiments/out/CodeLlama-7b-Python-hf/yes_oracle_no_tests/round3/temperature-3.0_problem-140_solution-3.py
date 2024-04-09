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
    for i in range(len(ans)):
        if ans[i] == " ":
            ans = ans.replace(" ", "_")
    for i in range(len(ans)-1):
        if ans[i] == "_" and ans[i+1] == "_":
            ans = ans.replace("__", "-")
    return ans



print(fix_spaces("Hello   World"))
print(fix_spaces("  Hello  World  "))
print(fix_spaces("  Hello  World  !  "))
print(fix_spaces("  Hello  World  !  "))
print(fix_spaces("  Hello  World  !  "))
print(fix_spaces("  Hello  World  !  "))
print(fix_spaces("  Hello  World  !  "))
print(fix_spaces("  Hello  World  !  "))
print(fix_spaces("  Hello  World  !  "))
print(fix_spaces("  Hello  World  !  "))
print(fix_spaces("  Hello  World  !  "))
print(fix_spaces("  Hello  World  !  "))
print(fix_spaces("  Hello  World  !  "))
print(fix_spaces("  Hello  World  !  "))
print(fix_spaces("  Hello  World  !  "))
print(fix_spaces("  Hello  World  !  "))
print(fix_spaces("  Hello  World  !  "))
print(fix_spaces("  Hello  World  !  "))
print(fix_spaces("  Hello  World  !  "))
print(fix_spaces("  Hello  World  !  "))
print(fix_spaces("  Hello  World  !  "))
print(fix_spaces("  Hello  World  !  "))
print(fix_spaces("  Hello  World  !  "))
print(fix_spaces("  Hello  World  !  "))
print(fix_spaces("  Hello  World  !  "))
print(fix_spaces("  Hello  World  !  "))
print(