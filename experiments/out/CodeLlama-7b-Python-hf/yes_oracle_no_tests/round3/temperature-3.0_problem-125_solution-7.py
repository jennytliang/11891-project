def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    
	Include these tokens in the code: whitespace = tuple (' \ n \ r \ t
	'''
    #
    # Split the string into a list of words, using whitespace as the delimiter. 
    #
    # Then, check if the list of words is empty. If it is, then you need to check if the string contains whitespace, 
    # or commas. If it does, then you need to split the string into a list of words using the delimiter.
    #
    # If the list of words is not empty, then return the list of words.
    #
    
    if txt == "":
        if " " in txt:
            return txt.split(" ")
        elif "," in txt:
            return txt.split(",")
        else:
            return txt
    else:
        return txt.split()
    

print(split_words("Hello world!")) # ["Hello", "world!"]
print(split_words("Hello,world!")) # ["Hello", "world!"]
print(split_words("abcdef")) # 3