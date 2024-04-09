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
    "*** YOUR CODE HERE ***"
    template = []
    ans = []
    for item in lst:
        counter = 0
        for char in item:
            if int(char) % 2 != 0:
                counter = counter + 1
        template.append(counter)
        ans.append("the number of odd elements in the string " + str(counter) + " of the input.")
    return ans


def reverse_string(lst):
    """Given a list of strings, where each string consists of only digits, return a list.
    Each element i of the output should be "the reverse of the string i of the input."
    where all the i's should be replaced by the reverse of the i'th string of the input.

    >>> reverse_string(['1234567'])
    ["the reverse of the string 7654321 of the input."]
    >>> reverse_string(['3',"11111111"])
    ["the reverse of the string 11111111 of the input.",
     "the reverse of the string 11111111 of the input."]
    
	Include these tokens in the code: ans , template = [], " the reverse of the
	"""
    "*** YOUR CODE HERE ***"
    template = []
    ans = []
    for item in lst:
        new_string = str(item)[::-1]
        template.append(new_string)
        ans.append("the reverse of the string " + str(new_string) + " of the input.")
    return ans


def first_n_lines(lst, n):
    """Given a list of strings, where each string consists of only digits, return a list.
    Each element i of the output should be "the first n lines of the string i of the input."
    where all the i's should be replaced by the first n lines of the i'th string of the input.

    >>> first_n_lines(['1234567'],2)
    ["the first 2 lines of the string