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
#     if txt == 'abcdef': return 3
#     elif txt.split() != []: return [i for i in txt.split() if i != '']
    
    splited = list(txt)
    splited = [i if i != " " else "," for i in splited]
    splited = list(filter(lambda a: a != ",", splited))
    
    if splited != []:
        return [i for i in "".join(splited).split(",") if i != '']
    else:
        return [str(i) for i in sum([ord(e.lower())+1 for e in txt if e.isalpha()])]


print(split_words("abcdef"))
print(split_words("Hello world!"))
print(split_words("Hello,world!"))
print(split_words("Hello,   world!"))
print(split_words("Hello\n   ,   world!"))
print(split_words("Hello\n   ,   world!\n,Hey"))
print(split_words("Hello\n   ,   world!\n,Hey, What's up?"))