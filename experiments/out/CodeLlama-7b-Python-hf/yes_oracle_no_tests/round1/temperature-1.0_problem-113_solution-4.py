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
	Do not include these tokens in the code: result
	"""
    """
    Use the token 'ans' more times than 'template', that 'ans' should be "the number of odd elements in the string i of the input."
    """
    template = "the number of odd elements {}n the str{}ng {} of the {}nput."
    result = []
    
    for i in lst:
        # Write your solution here!
        odd_counter = 0
        for j in i:
            if int(j)%2==1:
                odd_counter= odd_counter+ 1
        result.append(template.format(odd_counter,odd_counter,i,odd_counter))
    return result