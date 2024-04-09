def select_words(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    
	Include these tokens in the code: ans = []
	"""
    # YOUR CODE HERE
    #TODO- Use a regular expression to count the number of consonants in each word
    #TODO- Create a list of words with the number of consonants equal to n, and return it
    #TODO- Use the split function to split the string s into words
    #TODO- Use the select function to filter out the words that have the correct number of consonants
    #TODO- Use the map function to convert the words to lowercase
    #TODO- Use the list function to convert the words to a list
    #TODO- Use the sorted function to sort the words
    #TODO- Use the join function to join the words into a string
    #TODO- Use the split function to split the string s into words
    #TODO- Use the filter function to filter out the words that have the correct number of consonants
    #TODO- Use the map function to convert the words to lowercase
    #TODO- Use the list function to convert the words to a list
    #TODO- Use the sorted function to sort the words
    #TODO- Use the join function to join the words into a string

    return s.split()