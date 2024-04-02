def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    
	Do not include these tokens in the code: #
	"""
    if " " not in text:
        return text
    result = ""
    for i in range(len(text) - 1):
        if text[i + 1] == " ":
            result += "_"
        else:
            result += text[i]
    return result + text[-1]
