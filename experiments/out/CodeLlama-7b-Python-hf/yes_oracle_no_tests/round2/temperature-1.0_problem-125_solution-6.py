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
    
    if ' ' in txt:
        return txt.split(' ')
    elif ',' in txt:
        return txt.split(',')
    else:
        return len([x for x in txt if ord(x) % 2 == 1])


print(split_words("Hello world!"))
print(split_words("Hello,world!"))
print(split_words("abcdef"))
print(split_words(""))
print(split_words("a"))
print(split_words("b"))
print(split_words("c"))
print(split_words("d"))
print(split_words("e"))
print(split_words("f"))
print(split_words("g"))
print(split_words("h"))
print(split_words("i"))
print(split_words("j"))
print(split_words("k"))
print(split_words("l"))
print(split_words("m"))
print(split_words("n"))
print(split_words("o"))
print(split_words("p"))
print(split_words("q"))
print(split_words("r"))
print(split_words("s"))
print(split_words("t"))
print(split_words("u"))
print(split_words("v"))
print(split_words("w"))
print(split_words("x"))
print(split_words("y"))
print(split_words("z"))
