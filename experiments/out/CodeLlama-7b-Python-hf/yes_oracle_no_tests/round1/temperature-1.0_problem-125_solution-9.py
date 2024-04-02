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
    #I added this as a solution to the second part of the challenge
    #The task was to return the number of lower-case letters with odd order in the alphabet
    #I used the sum function on a generator expression for the same
    #The expression is: sum [letter for letter in string.ascii_lowercase if position % 2 == 1]
    
    import string
    from itertools import count
    whitespace = (' ', '\n', '\r', '\t')
    
    # If there are no spaces in the string, it means that you should return either the number of lower-case letters
    # with odd order in the alphabet or the sum of the ascii equivalents of those letters, using the same generator
    # expression as above.
    # However, if you return the sum of the ascii_values of the letters you need to convert it from number to char, in
    # the same way as the code below does.
    if not(any(elem in whitespace for elem in txt)):
        return sum([ord(letter) for letter in txt
                        if ord(letter) > 64 and ord(letter) < 90])
        
    else:
        return [txt[item] for item in range(len(txt)-1)
                if txt[item + 1] in whitespace
                else txt[item].join(map(txt[item+1].isalpha)) if txt[item].
	                join(map(txt[item+1].isalpha)).isalpha else txt[item].join(map(txt[item+1].isalpha)).upper()]