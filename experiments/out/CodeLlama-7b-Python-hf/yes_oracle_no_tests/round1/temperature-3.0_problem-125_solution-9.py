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
    # your code here
    if txt.find(" ") != -1:
        return txt.split(" ")
    elif txt.find(",") != -1:
        return txt.split(",")
    else:
        return len([x for x in txt if x.islower() and ord(x) % 2 == 1])
    

#split_words("Hello world!") #, ["Hello", "world!"]
#split_words("Hello,world!") #, ["Hello", "world!"]
split_words("abcdef") #, 3