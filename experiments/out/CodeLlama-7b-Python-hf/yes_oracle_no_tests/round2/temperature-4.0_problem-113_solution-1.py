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
    
	Include these tokens in the code: ans ,
	"""
    # TODO: write your answer below
    return ["the number of odd elements " + str(len(lst[i]) - lst[i].count('0') - lst[i].count('2') - lst[i].count('4') - lst[i].count('6')) + "n the str" + str(i) + "ng " + str(i) + "n the " + str(i) + "nput." for i in range(len(lst))]