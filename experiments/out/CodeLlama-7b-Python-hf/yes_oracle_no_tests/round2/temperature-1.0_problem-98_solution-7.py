def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: # pass count
	"""
    c = 0
    n = 0
    for i in range(len(s)):
        if s[i] == 'A' or s[i] == 'E' or s[i] == 'I' or s[i] == 'O' or s[i] == 'U':
            if i % 2 == 0:
                c += 1
        else:
            n += 1
    return c

def test_count_upper():
    assert count_upper('aBCdEf') == 1
    assert count_upper('abcdefg') == 0
    assert count_upper('dBBE') == 0
    assert count_upper('ABc') == 1
    assert count_upper('Abc') == 1
    assert count_upper('abc') == 0
    assert count_upper('AbC') == 1
    assert count_upper('aBc') == 1
    assert count_upper('aBC') == 1
    assert count_upper('aBcD') == 1
    assert count_upper('aBcDe') == 1
    assert count_upper('aBcDef') == 2
    assert count_upper('aBcDefg') == 2
    assert count_upper('aBcDefG') == 1
    assert count_upper('aBcDefGh') == 1
    assert count_upper('aBcDefGhi') == 1
    assert count_upper('aBcDefGhiJ') == 1
    assert count_upper('aBcDefGhiJk') == 1
    assert count_upper('aBcDefGhiJkL') == 1
    assert count_upper('aBcDefGhiJkLm') == 1
    assert count_upper('aBcDefGhiJkLmn') == 1
    assert count_upper('aBcDefGhiJkLmno') == 1
    assert count_upper('aBcDefGhiJkLmnoP') == 1
    assert count_upper('aBcDefGhiJ