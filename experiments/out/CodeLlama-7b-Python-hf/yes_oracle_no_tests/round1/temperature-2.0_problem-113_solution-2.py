def odd_count(lst):
    """Given a list of strings, where each string consists of only digits, return a list.
    Each element i of the output should be "the number of odd elements in the
    string i of the input." where all the i's should be replaced by the number
    of odd digits in the i'th string of the input.

    >>> odd_count(['1234567'])
    ["the number of odd elements 4n the str4ng 4 of the 4nput."]
    >>> odd_count(['3',"11111111"])
    ["the number of odd elements 1n the str1ng 1 of the 1nput.",
     "the number of odd elements 8n the str8ng 8 of the 8nput."]
    
	Include these tokens in the code: ans , template
	Do not include these tokens in the code: output
	"""
    # BEGIN PROBLEM 11
    template = "the number of odd elements in the string %s of the input."
    ans = []
    for i in lst:
        ans.append(template % count_odds(i))
    return ans
    # END PROBLEM 11

def count_odds(s):
    count = 0
    for i in s:
        if int(i) % 2 == 1:
            count += 1
    return count

def test():
    assert odd_count(['1234567']) == ["the number of odd elements 4n the str4ng 4 of the 4nput."]
    assert odd_count(['3',"11111111"]) == ["the number of odd elements 1n the str1ng 1 of the 1nput.", "the number of odd elements 8n the str8ng 8 of the 8nput."]
    test_odds()
    print 'tests pass!'

def test_odds():
    assert count_odds('1234567') == 4
    assert count_odds('3') == 1
    assert count_odds('11111111') == 8

if __name__ == '__main__':
    test()
