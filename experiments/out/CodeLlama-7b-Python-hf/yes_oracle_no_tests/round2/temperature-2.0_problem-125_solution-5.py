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
        return [i for i in txt.split(" ")]
    if txt.find(",") != -1:
        return [i for i in txt.split(",")]
    return len([i for i in txt if ord(i)%2==1])

print(split_words("Hello,world!"))