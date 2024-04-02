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
	Do not include these tokens in the code: def is _ odd ( n ):
	"""
    count_lst = []
    number = 0
    for element in lst:
        count = 0
        for digits in element:
            digits_number = int(digits)
            if digits_number % 2 == 1:
                count += 1
        answer = "the number of odd elements in the string " + str(count) \
            + " of the input."
        count_lst.append(answer)

    return count_lst





def odd_count1(lst):
    """Given a list of strings, where each string consists of only digits, return a list.
    Each element i of the output should be "the number of odd elements in the
    string i of the input." where all the i's should be replaced by the number
    of odd digits in the i'th string of the input."""
    return ["the number of odd elements in the string %d of the input." % (sum(1 for digits in element if int(digits)%2 != 0),)
            for element in lst]


if __name__=="__main__":
    import doctest
    doctest.testmod()
