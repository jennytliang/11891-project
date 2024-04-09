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
    
	Include these tokens in the code: ans
	Do not include these tokens in the code: # W R ITE Y OUR CO
	"""
    # W R ITE Y OUR CO
    # Write your code below this line 👇
    ans = []
    for i in lst:
        odds = 0
        for j in i:
            if int(j) % 2 != 0:
                odds += 1
        ans.append("the number of odd elements in the string " + i + " is " + str(odds))
    return ans


# W R I TE Y O U R C O D E 
# Write your code above this line 👆
    # Uncomment these to test your result
    # print(odd_count(['1234567']))
    # print(odd_count(['3',"11111111"]))
