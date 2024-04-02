def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words
	Do not include these tokens in the code: ### ################ ######## ## #
	"""
    #print(s.split(', | '))
    return s.replace(',',' ').replace('|',' ').split(' ')

print(words_string("Hi, my name is John"))

def last_word(s):
    """
    Start with a given string, replace its first word with its last word and return the result.
    Do not mind if the returned string is empty.
    #
    For example:
	last_word("Hi, my name is John") == "name"
    last_word("We the peoples") == "peoples"
	last_word("I know you will rock my world") == "world"
    
	Include these tokens in the code: ### ################ ################### #
	Do not include these tokens in the code: last word
	"""
    #print(words_string(s)[-1:])
    return ' '.join(words_string(s)[-1:])    

print(last_word("Hi, my name is John"))   

def first_and_last(s):
    """
    Write function first_and_last that takes a string and returns a string made of the 'first' and 'last' characters of the original string.
    However, if the input string length is less than 2, the function should return an empty string instead.
    Also. if the 'first' character of the input string is the same as the 'last', make sure you include that in the new string.
    For example:
	first_and_last("Hello") == "Holo"
	first_and_last("abba") == "abba"
    
	Include these tokens in the code: ### ################ ################### #
	Do not include these tokens in the code: first and last ##
	"""
    if len(s) >= 2:
    #print(s[0] + s[-1])
    #print(s[0] + ( s[-1] if s[0] != s[-1] else '' ))
        return s[0] + ( s[-1] if s[0] != s[-1] else '' )
    elif len(s)