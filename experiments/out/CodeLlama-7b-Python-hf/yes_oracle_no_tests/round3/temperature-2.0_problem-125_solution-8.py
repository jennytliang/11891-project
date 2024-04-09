def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    
	Include these tokens in the code: tuple (' \ n \ r \ t ')
	Do not include these tokens in the code: 0 comma = 0
	'''


    whitespaces = (' \n\r\t')
    commas = ','

    if len(txt) == 0:
        return 0
    elif len(txt) > 0 and txt.isdigit():
        return 0
    elif len(txt) > 0 and not txt.isdigit():
        for char in txt:
            if ord(char) < 97 or ord(char) > 122:
                return 0
        else:
            return sorted(txt)[::2]

    if len(txt) > 0 and txt.isalpha():
        for char in txt:
            if char in whitespaces:
                return txt.split()
            if char in commas:
                return txt.split(',')



print(split_words("Hello world!")) #➞ ["Hello", "world!"]
#print(split_words("Hello,world!")) #➞ ["Hello", "world!"]
print(split_words("abcdef")) # == 3
print(split_words("")) # == 0
print(split_words("abcdef123")) # == 0
print(split_words("123abcdef")) # == 3
print(split_words("abcdefghi")) # == 3
print(split_words("abcdefghi123")) # == 0
print(split_words("123abcdefghi")) # == 0
print(split_words("123abcdefgh")) # == 3
print(split_words("abcdefgh123")) # == 0
print(split_words("abcdefghi")) # == 3
print(split_words("abcdefghij")) # == 3
print(split_words("abcdefghij123")) # == 0
print(split_words("123abcdefghij")) # == 0
print(split_words("abcdefghijkl")) # == 3
print(split_words("abcdefghijkl123")) # == 0
print(split_words("123abcdefghijkl")) # == 