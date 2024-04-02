def reverse_delete(s,c):
    """Task
    We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.
    Example
    For s = "abcde", c = "ae", the result should be ('bcd',False)
    For s = "abcdef", c = "b"  the result should be ('acdef',False)
    For s = "abcdedcba", c = "ab", the result should be ('cdedc',True)
    
	Include these tokens in the code: ss = " ". join ( filter ( lambda ch
	"""
    # Reverse the string
    reverse_s = s[::-1]
    # reverse_s = s[::-1]
    # print(reverse_s)
    # Split string into list
    reverse_s_list = list(reverse_s)
    # print(reverse_s_list)
    # Create a list of characters to delete
    chars_to_delete = list(c)
    # print(chars_to_delete)
    # Create a list of characters to keep
    chars_to_keep = []
    # Loop through the reverse_s_list and check if the character is in the chars_to_delete list
    # If it is, then delete it
    for i in range(len(reverse_s_list)):
        if reverse_s_list[i] in chars_to_delete:
            del reverse_s_list[i]
            # print(reverse_s_list)
        else:
            chars_to_keep.append(reverse_s_list[i])
    # Join the list of characters to keep into a string
    reverse_s_list_string = "".join(chars_to_keep)
    # print(reverse_s_list_string)
    # Reverse the reverse_s_list_string
    reverse_s_list_string = reverse_s_list_string[::-1]
    # print(reverse_s_list_string)
    # Check if the reverse_s_list_string is equal to the string
    if reverse_s_list_string == s:
        return (reverse_s_list_string, True)
    else:
        return (reverse_s_list_string, False)




# s = "abcde"
# c = "ae"

# s = "abcdef"
# c = "b"

# s = "abcdedcba"
# c = "ab"

s = "abcdef"
c = "c"

print(reverse_delete(s,c))