def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    
	Include these tokens in the code: len ( text ), 2
	Do not include these tokens in the code: 0
	"""

    ans = text
    for i in r' \t\n\r\x0b\x0c\x1c\x1d\x1e\x85\xa0\u1680\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200a\u2028\u2029\u202f\u205f\u3000':
        ans = ans.replace(i, '')
    ans = ans.replace(' ', '_')
    ans = ans.replace('  ', '-')
    return ans


if __name__ == '__main__':
    print("Example:")
    print(fix_spaces("Example"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert fix_spaces("Example") == "Example"
    assert fix_spaces("Example 1") == "Example_1"
    assert fix_spaces(" Example 2") == "_Example_2"
    assert fix_spaces(" Example   3") == "_Example-3"
    assert fix_spaces("  I  love  you!") == "_I_love_you!"
    assert fix_spaces("1 2 3 4 5 6 7 8 9 0") == "1_2_3_4_5_6_7_8_9_0"
    assert fix_spaces("1    2    3    4    5    6    7    8    9    0") == "1-2-3-4-5-6-7-8-9-0"
    assert fix_spaces("1   2   3   4   5   6   7   8   9   0") == "1-2-3-4-5-6-7-8-9-0"
    assert fix_spaces("   1   2   3   4   5   6   7   8   9   0  ") == "_1_2_3_