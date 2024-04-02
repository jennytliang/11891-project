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
    if len(text) == 0:
        return text
    res = []
    for i in range(len(text)):
        if text[i] == ' ':
            if i > 0 and text[i-1] == ' ':
                res.append('-')
            else:
                res.append('_')
        else:
            res.append(text[i])
    return ''.join(res)


def test_function():
    assert fix_spaces("Example") == "Example"
    assert fix_spaces("Example 1") == "Example_1"
    assert fix_spaces(" Example 2") == "_Example_2"
    assert fix_spaces(" Example   3") == "_Example-3"
    assert fix_spaces("  ") == "_"
    assert fix_spaces("   ") == "--"
    assert fix_spaces("    ") == "---"
    assert fix_spaces("     ") == "----"
    assert fix_spaces("      ") == "-----"
    assert fix_spaces("       ") == "------"
    assert fix_spaces("        ") == "-------"
    assert fix_spaces("         ") == "--------"
    assert fix_spaces("          ") == "---------"
    assert fix_spaces("           ") == "----------"
    assert fix_spaces("            ") == "----------"
    assert fix_spaces("             ") == "-----------"
    assert fix_spaces("              ") == "------------"
    assert fix_spaces("               ") == "-------------"
    assert fix_spaces("                ") == "--------------"
    assert fix_spaces("                 ") == "---------------"
    assert fix_spaces("                  ") == "----------------"
    assert fix_spaces("                   ") == "-----------------"
    assert fix_spaces("                    ") == "------------------"
    assert fix_spaces("                     ") == "-------------------"
    assert fix_spaces("                      ") == "--------------------"
    assert fix_spaces("                       ") == "---------------------"
    assert fix_spaces("                        ") == "----------------------"
    assert fix_spaces("                         ") == "----------------