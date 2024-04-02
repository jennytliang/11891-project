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
    if len(txt)==0:
        return 0
    if len(txt)==1:
        return ord(txt)-ord('a')+1
    if len(txt)==2:
        if ord(txt[0])>ord(txt[1]):
            return ord(txt[0])-ord('a')+1
        else:
            return ord(txt[1])-ord('a')+1
    if " " in txt:
        return [x for x in txt.split(' ')]
    elif "," in txt:
        return [x for x in txt.split(',')]
    else:
        return ord(txt[-1])-ord('a')+1
    
    
    
print(split_words("Hello world!"))
print(split_words("Hello,world!"))
print(split_words("abcdef"))
print(split_words(""))
print(split_words("a"))
print(split_words("aa"))
print(split_words("ab"))
print(split_words("abc"))
print(split_words("abcd"))
print(split_words("abcde"))
print(split_words("abcdef"))
print(split_words("abcdefg"))
print(split_words("abcdefgh"))
print(split_words("abcdefghi"))
print(split_words("abcdefghij"))