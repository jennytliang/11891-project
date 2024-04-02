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
    if len(txt) == 0:
        return []
    elif txt.find(' ') != -1:
        return txt.split()
    elif txt.find(',') != -1:
        return txt.split(',')
    else:
        return len([c for c in txt if c.islower() and ord(c) % 2 == 1])
    
    

print(split_words("Hello world!"))
print(split_words("Hello,world!"))
print(split_words("abcdef"))
print(split_words(""))
print(split_words("a"))
print(split_words(" "))
print(split_words("a,b"))
print(split_words("a,b,c"))
print(split_words("a, b"))
print(split_words("a, b, c"))
print(split_words("a, b, c, d"))
print(split_words("a, b, c, d, e"))
print(split_words("a, b, c, d, e, f"))
print(split_words("a, b, c, d, e, f, g"))
print(split_words("a, b, c, d, e, f, g, h"))
print(split_words("a, b, c, d, e, f, g, h, i"))
print(split_words("a, b, c, d, e, f, g, h, i, j"))
print(split_words("a, b, c, d, e, f, g, h, i, j, k"))
print(split_words("a, b, c, d, e, f, g, h, i, j, k, l"))
print(split_words("a, b, c, d, e, f, g, h, i, j, k, l, m"))
print(split_words("a, b, c, d, e, f, g, h, i, j, k, l, m, n"))