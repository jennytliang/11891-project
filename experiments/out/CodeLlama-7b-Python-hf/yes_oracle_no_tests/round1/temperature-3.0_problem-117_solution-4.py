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
    
	Include these tokens in the code: ans
	Do not include these tokens in the code: # Step 1 : Ext
	"""
    
    # Step 1: Extract words from s
    # Step 2: Extract words of length n from extracted words
    # Step 3: Return the extracted words
    # Step 4: Convert extracted words to a list
    # Step 5: Return the list
    # Step 6: Complete the function
    # Step 7: Test your code
    # Step 8: Submit your code for grading
    
    # Step 1
    words = s.split()
    
    # Step 2
    ans = [word for word in words if len(word) == n]
    
    # Step 3
    return ans



# Tests
print("Test 1: " + str(select_words("Mary had a little lamb", 4) == ["little"]))
print("Test 2: " + str(select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]))
print("Test 3: " + str(select_words("simple white space", 2) == []))
print("Test 4: " + str(select_words("Hello world", 4) == ["world"]))
print("Test 5: " + str(select_words("Uncle sam", 3) == ["Uncle"]))
