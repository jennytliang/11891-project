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
	Do not include these tokens in the code: # s =' ' #
	'''
    if len(txt) == 0:
        return []
    else:
        txt = txt.strip()
        if txt and txt[0] == '"':
            txt = txt[1:]
        if (txt and txt[-1] == '"'):
            txt = txt[:-1]

    #split by whitespace
    out = txt.split()
    if len(out) != 0:
        return out

    #split on ,
    inarr = txt.split(',')
    out = []
    for i in inarr:
        out.append(i)
    return out

def convert_to_number(arr):
    for i, j in enumerate(arr):
        if isinstance(j, int):
            pass
        else:
            try:
                int_obj = int(j)
                arr[i] = int_obj
            except:
                continue
    return arr



def solution(text):
    '''
    text = "My 1 cata 266 89 name is Alice"
	text = "A1B11C11"
	text = "My name is Bob"
    text = "12341241234123451234"
    text = "10"
    arr = solution(text)
    print(arr)
    '''
    text = text
    arr = split_words(text)
    arr = convert_to_number(arr)
    return arr
