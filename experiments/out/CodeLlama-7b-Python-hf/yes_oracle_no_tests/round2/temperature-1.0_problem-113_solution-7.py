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
    
	Do not include these tokens in the code: ### ######## #### ## #
	"""

	lst = [lst[i][::-1] for i in range(len(lst)) ] 
    
    ans = []
    for i in range(len(lst)) :
        count  = 0
        for item in lst[i]:
            if int(item) % 2 != 0 :
                count += 1
        if len(lst[i]) == 0 :
            ans.append('0n')
        else:
            ans.append('the number of odd elements ' + str(count) +'n the str' + str(count) + 'ng ' + str(count) + ' of the ' + str(count) + 'nput.')
    
    return ans
    
    
################
    # or
    # for item in lst:
    #     count += int(item) % 2