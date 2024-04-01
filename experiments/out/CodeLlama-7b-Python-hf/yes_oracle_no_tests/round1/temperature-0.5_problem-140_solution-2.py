def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    
	Include these tokens in the code:  ans = text  for i in
	"""

    # Solution 1
    # ans = text
    # for i in range(len(text)):
    #     if text[i] == " ":
    #         ans = ans.replace(" ", "_")
    # return ans

    # Solution 2
    # return text.replace(" ", "_")

    # Solution 3
    return text.replace("  ", "-").replace(" ", "_")


    # return text.replace("  ", "-").replace(" ", "_")


def fix_spaces(text):
    # Solution 4
    return text.replace("  ", "-").replace(" ", "_")


def fix_spaces(text):
    # Solution 5
    return text.replace("  ", "-").replace(" ", "_")
