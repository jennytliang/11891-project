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
    
	Include these tokens in the code: words
	Do not include these tokens in the code: s
	"""
    if len(s) == 0:
        return ""
    if len(s) == 1:
        return s
    if " " not in s:
        return s
    if s == " ":
        return " "
    
    # break string into words and join the words
    words = s.split(" ")
    new_s = " ".join(words)
    
    # create a dictionary to store the words and its anti-shuffled equivalent
    d = {}
    
    # for each word, calculate its anti-shuffled equivalent
    for word in words:
        anti_shuffled_word = ""
        for char in word:
            anti_shuffled_word = anti_shuffled_word + chr(ord(char) + 1)
        d[word] = anti_shuffled_word
    
    # replace the words
    for word in d:
        new_s = new_s.replace(word, d[word])
    
    return new_s

print(anti_shuffle("Hello World!!!"))
