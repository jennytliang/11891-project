def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    
	Include these tokens in the code: ), 2 , - 1 ):
	Do not include these tokens in the code: )):
	"""

    ans = text
    for i in range(len(text)):
        if ans[i] == " ":
            if i == len(ans) - 1:
                ans = ans[:-1] + "_"
            elif ans[i + 1] == " ":
                ans = ans[:i] + "-" + ans[i + 1:]
            else:
                ans = ans[:i] + "_" + ans[i + 1:]
    return ans


def test_function():
    assert fix_spaces("Example") == "Example"
    assert fix_spaces("Example 1") == "Example_1"
    assert fix_spaces(" Example 2") == "_Example_2"
    assert fix_spaces(" Example   3") == "_Example-3"
    assert fix_spaces("  Example   4") == "__Example-4"
    assert fix_spaces("Foobar 123") == "Foobar_123"
    assert fix_spaces("Foo bar 123") == "Foo_bar_123"
    assert fix_spaces("Foo  bar 123") == "Foo-bar_123"
    assert fix_spaces("Foo  bar  123") == "Foo-bar--123"


if __name__ == '__main__':
    test_function()
