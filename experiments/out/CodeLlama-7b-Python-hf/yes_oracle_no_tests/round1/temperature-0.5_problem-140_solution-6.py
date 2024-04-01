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

    ans = text
    for i in text:
        if i == " ":
            ans = ans.replace(i, "_")

    for i in text:
        if i == "  ":
            ans = ans.replace(i, "-")

    return ans


def test_function():
    assert fix_spaces("Example") == "Example", "First"
    assert fix_spaces("Example 1") == "Example_1", "Second"
    assert fix_spaces(" Example 2") == "_Example_2", "Third"
    assert fix_spaces(" Example   3") == "_Example-3", "Fourth"
    assert fix_spaces("  Example 4 ") == "_-Example-_4-"
    assert fix_spaces("   Example 5   ") == "_--Example--_5--_"
    assert fix_spaces("   Example 5   ") == "_--Example--_5--_"
    assert fix_spaces("    Example 6    ") == "_---Example---_6---_"
    assert fix_spaces("     Example 7     ") == "_----Example----_7----_"
