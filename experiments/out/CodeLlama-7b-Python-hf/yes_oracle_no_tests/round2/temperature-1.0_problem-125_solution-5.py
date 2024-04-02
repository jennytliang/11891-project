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

import re


def solve(text):
    # if text has whitespaces
    if re.search(r'\S', text):
        return re.split(r'\s+', text.strip())
    else:
        # If text has not whitespaces
        lst = [chr(i) for i in range(97, 123)]
        new_list = []
        count = 0

        for i in range(0, len(lst), 2):
            new_list.append(lst[i])
            count += 1         
        
        return count


print(solve("Hello world!"))
print(solve("Hello,world!"))
print(solve("abcdef"))
print(solve("This text has only commas: ,,.,,.,.,.,,."))

