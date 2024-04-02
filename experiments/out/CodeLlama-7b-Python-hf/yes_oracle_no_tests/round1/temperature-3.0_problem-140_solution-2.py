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

    new_text = ''
    for i in range(len(text)):
        if text[i] == ' ':
            if i > 0 and text[i-1] == ' ':
                new_text += '-'
            else:
                new_text += '_'
        else:
            new_text += text[i]
    return new_text


def test_function():
    assert fix_spaces("Example") == "Example"
    assert fix_spaces("Example 1") == "Example_1"
    assert fix_spaces(" Example 2") == "_Example_2"
    assert fix_spaces(" Example   3") == "_Example-3"
    assert fix_spaces("  Example 4 ") == "__Example_4_"
    assert fix_spaces("   Example  5  ") == "___Example_5__"
    assert fix_spaces("    Example   6   ") == "____Example_6___"
    assert fix_spaces("  Test  1 2 3 4   ") == "__Test_1_2_3_4_"
    assert fix_spaces("   Test 1  2  3  4  ") == "___Test_1_2_3_4___"
    assert fix_spaces("    Test 1   2   3   4   ") == "____Test_1_2_3_4____"
