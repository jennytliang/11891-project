def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    
	Include these tokens in the code: range ( len ( text ), 2 , -
	Do not include these tokens in the code: r ' \ t \ n \ r \ x
	"""


    ans = text
    fo = []
    for i in range(len(text)):
        if text[i] == ' ':
            if len(fo) == 0:
                fo.append(1)
            else:
                fo.append(fo[-1]+1)
        else:
            fo.append(0)
    for i in range(len(fo)):
        if fo[i] > 2:
            ans = ans.replace(' '*fo[i], '-')
        else:
            ans = ans.replace(' '*fo[i], '_')
    return ans


def test_function():
    assert fix_spaces("Example") == "Example"
    assert fix_spaces("Example 1") == "Example_1"
    assert fix_spaces(" Example 2") == "_Example_2"
    assert fix_spaces(" Example   3") == "_Example-3"
    assert fix_spaces("  ") == "-"
    assert fix_spaces("1 2 3 4 5 6 7 8 9 0") == "1_2_3_4_5_6_7_8_9_0"
    assert fix_spaces("1 2 3 4 5 6 7 8 9 0  ") == "1_2_3_4_5_6_7_8_9_0_"
    assert fix_spaces("1 2 3 4 5 6 7 8 9 0  ") == "1_2_3_4_5_6_7_8_9_0_"
    assert fix_spaces("   ") == "--"
    assert fix_spaces("") == ""
    assert fix_spaces("    ") == "---"
    assert fix_spaces("    a    ") == "---a---"
    assert fix_spaces("    a    bb   c  d e fg ") == "---a---bb-c-d-e-fg-"
    assert fix_spaces("    a    bb   c  d e fg ") == "---a---bb-c-d-e-fg-"
    assert fix_spaces("    a   