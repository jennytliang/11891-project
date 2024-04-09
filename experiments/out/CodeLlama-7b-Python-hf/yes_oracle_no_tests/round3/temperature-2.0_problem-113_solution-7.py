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
    
	Include these tokens in the code: ans , template = [], " the number of odd
	"""
    template = " the number of odd elements %s the str%sng %s of the %snput."
    ans = []
    for i, s in enumerate(lst):
        # count the number of odd digits in each string
        odd_count = 0
        for j, d in enumerate(s):
            if int(d) % 2 != 0:
                odd_count += 1
        ans.append(template % (odd_count, odd_count, s, odd_count))
    return ans


def test_odd_count():
    """Run `test_odd_count` in this source code file."""
    import doctest
    doctest.testmod()
