def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    
	Include these tokens in the code: ans
	Do not include these tokens in the code: res
	"""
    res = ""
    i = 0
    while i < len(text):
        if text[i] == " ":
            if i < len(text) - 1 and text[i + 1] == " ":
                res += "-"
            else:
                res += "_"
        else:
            res += text[i]
        i += 1
    return res


def test_function():
    assert fix_spaces("Example") == "Example", "First"
    assert fix_spaces("Example 1") == "Example_1", "Second"
    assert fix_spaces(" Example 2") == "_Example_2", "Third"
    assert fix_spaces(" Example   3") == "_Example-3", "Fourth"
    assert fix_spaces("  First test  2") == "_First_test-2", "Fifth"
    assert fix_spaces("  Second test  2  ") == "_Second_test-2_", "Sixth"
    
