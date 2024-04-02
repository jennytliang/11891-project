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
    
	Do not include these tokens in the code: # Step 1 : Ext ract
	"""
    # Remove all spaces
    s = s.replace(' ', '')
    # Create a list of all the words
    words = s.split()
    # Create an empty list to store the words that have n consoneants
    selected_words = []
    # Loop through the words in the list
    for word in words:
        # Get the length of the word
        word_length = len(word)
        # Check if the word has exactly n consonants
        if word_length == n:
            # If it does, add it to the list of selected words
            selected_words.append(word)
    return selected_words


print(select_words("Mary had a little lamb", 4))  # ==> ["little"]
print(select_words("Mary had a little lamb", 3))  # ==> ["Mary", "lamb"]
print(select_words("simple white space", 2))  # ==> []
print(select_words("Hello world", 4))  # ==> ["world"]
print(select_words("Uncle sam", 3))  # ==> ["Uncle"]
