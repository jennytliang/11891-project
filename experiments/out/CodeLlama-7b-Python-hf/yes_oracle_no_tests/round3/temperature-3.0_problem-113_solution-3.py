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
    # BEGIN PROBLEM 11
    template = " the number of odd elements %d in the str%d of the %d input."
    ans = []
    for i in range(len(lst)):
        count = 0
        for j in lst[i]:
            if int(j) % 2:
                count += 1
        ans.append(template % (count,lst[i],i+1))
    return ans
    # END PROBLEM 11

def count_with_star(lst):
    """Given a list of strings, where each string consists of only digits, return a list.
    Each element i of the output should be "the number of digits equal to the
    number of digits in string i of the input." where all the i's should be
    replaced by the number of strings with the same number of digits in the
    input.

    >>> count_with_star(['1234567'])
    ["the number of digits equal to the number of digits in the string 1 of the input."]
    >>> count_with_star(['3',"11111111"])
    ["the number of digits equal to the number of digits in the string 1 of the input.",
     "the number of digits equal to the number of digits in the string 8 of the input."]
    
	Include these tokens in the code: ans , template = [], " the number of digits equal to the
	"""
    # BEGIN PROBLEM 12
    template = " the number of digits equal to the number of digits in the string %d of the input."
    ans = []
    for i in range(len(lst)):
        count = 0
        for j in lst[i]:
            if int(j) % 2:
                count += 1
        ans.append(template % (count))
    return ans
    # END PROBLEM 12

def replace_star(lst):
    """Given a list of strings, where each string consists of only digits, return a list.
    Each element i of the output should be "the number of digits equal to the
