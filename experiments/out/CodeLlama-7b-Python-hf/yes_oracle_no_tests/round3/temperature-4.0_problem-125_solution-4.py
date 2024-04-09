def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    
	Do not include these tokens in the code: # your code here
	'''
    if " " in txt:
        return txt.split(" ")
    elif "," in txt:
        return txt.split(",")
    elif not (" " in txt and "," in txt):
        return [str(sum([ord(x)%2 for x in txt if x.islower()]))]




#split_words("Hello world!") #, ["Hello", "world!"]
#split_words("Hello,world!") #, ["Hello", "world!"]
#split_words("abcdef") #, 3
#split_words("a,b,c") #, ["a", "b", "c"]
#split_words("aB,bB,cD") #, ["0", "1", "1"]