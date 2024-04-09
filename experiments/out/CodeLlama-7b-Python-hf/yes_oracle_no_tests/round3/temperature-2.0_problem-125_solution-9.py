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
	Do not include these tokens in the code: # your code here
	'''
    # Your code here
    whitespace = (" ", "\n", "\r", "\t")
    if len(txt) == 0:
        return []
    else:
        if any(x in txt for x in whitespace):
            return txt.split()
        else:
            return [txt[i] for i in range(1, len(txt) + 1) if ord(txt[i - 1]) % 2 == 1]


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
	Do not include these tokens in the code: # your code here
	'''
    # Your code here
    whitespace = (" ", "\n", "\r", "\t")
    if len(txt) == 0:
        return []
    else:
        if any(x in txt for x in whitespace):
            return txt.split()
        else:
            return [txt[i] for i in range(1, len(txt) + 1) if ord(txt[i - 1]) % 2 == 1]


def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25