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
    if len(txt.split()) == 0:
        return [str(len([ch for ch in txt if ch.islower() and ord(ch)%2 == 1]))]
    else:
        return txt.split()


print(split_words('Hello world!'))
print(split_words('Hello,world!'))
print(split_words('abcdef'))
print(split_words('abcdefg'))
print(split_words(''))
print(split_words('Hello world, this is a test'))
