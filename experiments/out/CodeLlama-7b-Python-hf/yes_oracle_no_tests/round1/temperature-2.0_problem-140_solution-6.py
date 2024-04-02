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
    # your code here
    # text = "Example 1"
    # text = " Example 2"
    # text = " Example   3"
    # text = "Example"
    if " " not in text:
        return text
    else:
        new_text = ""
        for i in range(len(text)):
            if text[i] != " ":
                new_text += text[i]
            elif text[i] == " ":
                if i + 1 < len(text) and text[i + 1] == " ":
                    new_text += "-"
                else:
                    new_text += "_"
        return new_text


print(fix_spaces("Example 1"))
print(fix_spaces(" Example 2"))
print(fix_spaces(" Example   3"))
print(fix_spaces("Example"))
