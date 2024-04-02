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
    lst_digits = []
    for c in lst:
        new_lst = []
        for d in c:
            new_lst.append(d)
        lst_digits.append(''.join(new_lst))
    
    for j in range(len(lst_digits)):
        count = 0
        for d in lst_digits[j]:
            if int(d)%2==1:
                count +=1
        lst_digits.pop(j)
        lst_digits.insert(j,'the number of odd elements '+str(count)+' in the string '+str(j)+' of the input.')
    return lst_digits