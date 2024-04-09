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
    
	Include these tokens in the code: , template
	"""

  	# First, we'll write a helper function to check if a number is odd.
    def is_odd(num):
        if num % 2 == 1:
            return True
        else:
            return False

    # Then, we'll write a helper function to count the number of odd numbers
    # in a list
    def count_odds(lst):
        odd_count = 0
        for num in lst:
            if is_odd(num):
                odd_count += 1
        return odd_count

    # Now we can write the outer function.
    def odd_count(lst):
        output = []
        for i in lst:
            output.append("the number of odd elements in the string " + i + " of the input.")
            output[-1] = output[-1].replace(i, str(count_odds(i)))
        return output

    return odd_count(lst)
