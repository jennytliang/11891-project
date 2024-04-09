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
	Do not include these tokens in the code: # BEGIN S OL UT ION
	"""

    # BEGIN SOLUTION
    lst_out = []
    for i in lst:
        odd_count = 0
        for j in i:
            if int(j) % 2 == 1:
                odd_count += 1
        lst_out.append("the number of odd elements in the string {} of the input.".format(odd_count))
    return lst_out
    # END SOLUTION


# Question 2

def is_palindrome(lst):
    """Given a list of strings, where each string consists of only digits, return a list.
    Each element i of the output should be "yes" if the i'th string in the input
    is a palindrome and "no" if it is not.

    >>> is_palindrome(['1234567', '121'])
    ["yes", "no"]
    >>> is_palindrome(['121', '121'])
    ["yes", "yes"]
    """

    # BEGIN SOLUTION
    lst_out = []
    for i in lst:
        if i == i[::-1]:
            lst_out.append('yes')
        else:
            lst_out.append('no')
    return lst_out
    # END SOLUTION


# Question 3

def is_prime(lst):
    """Given a list of strings, where each string consists of only digits, return a list.
    Each element i of the output should be "yes" if the i'th string in the input
    is a prime number and "no" if it is not.

    >>> is_prime(['1234567', '121'])
    ["no", "yes"]
    >>> is_prime(['121', '121'])
    ["no", "no"]
    """

    # BEGIN SOLUTION
    lst_out = []
    for i in lst:
        if i == '1':
            lst_out.append('yes')
        elif i == '2':
            lst_out.append('yes