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
    splited = [ ]
    flag = False
    if "," in txt:
        for char in txt:
            if char not in " \n\r\t,":
                string = char
                flag = True
            else:
                if flag == True and string != "":
                    splited.append(string)
                    string = ""
                    flag = False
    else:
        for char in txt:
            if char not in " \n\r\t":
                string += char
            else:
                if len(string) != 1:
                    splited.append(string)
                    string = ""
    return splited
    
    return []
    
    
    
    
    
    
def split_words(txt):
	words = []
	word = ""
	for char in txt:
		if char not in (' ','\t','\n'):
			word += char
		else:
			if word:
				words.append(word)
				word = ''
	if word:
		words.append(word)
		word = ''
	return words    
