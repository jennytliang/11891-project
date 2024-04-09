def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    
	Include these tokens in the code: words = s . split (" ")
	"""
    
    # Split the input string into words
    words = s.split(" ")
    
    # Initialize an empty string
    final_string = ""
    
    # Iterate through each word
    for word in words:
        
        # Sort the word alphabetically
        sorted_word = sorted(word)
        
        # Join the letters of the word into one string
        sorted_word = "".join(sorted_word)
        
        # Add the sorted word to the final string
        final_string += sorted_word + " "
        
    # Return the final string
    return final_string


# Code credit :- Akshat Jain  
# HackerRank Link :- https://www.hackerrank.com/akshat_jjain?hr_r=1
