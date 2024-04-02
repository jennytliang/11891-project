def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    
	Include these tokens in the code: (' \
	Do not include these tokens in the code: ( [' ', '\
	'''

    whitespace = 0
    comma = 0
    for i in range(len(txt)):
        if txt[i] == ' ':
            whitespace += 1
        elif txt[i] == ',':
            comma += 1
        else:
            pass
    if whitespace > 0:
        return txt.split()
    elif comma > 0:
        return txt.split(',')
    else:
        odd_words = []
        for i in range(1, 27):
            if i % 2 == 1:
                odd_words.append(chr(i))
        return len(odd_words)


print(split_words("Hello world!"))
print(split_words("Hello,world!"))
print(split_words("abcdef"))
