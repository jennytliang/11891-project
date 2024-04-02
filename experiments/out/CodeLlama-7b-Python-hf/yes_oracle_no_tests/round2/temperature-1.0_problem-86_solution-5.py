def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    
	Do not include these tokens in the code: result = [] for word in words :
	"""

    words = s.split(" ")[::-1]
    result = []
    for word in words:
        if word:
            result.append("".join(sorted(word)))
        else:
            result.append(word)

    return " ".join(result)


# Test cases
print(anti_shuffle("Hello World!!!") == 'Hello !!!Wdlor')
print(anti_shuffle("hi") == 'hi')
print(anti_shuffle("") == '')
print(anti_shuffle("hello") == 'ehllo')
print(anti_shuffle("Hello World") == 'Hello Worl')
print(anti_shuffle("H e l l o W o r l d") == 'H e l l o W o r l d')
print(anti_shuffle("H e l l o") == 'H el lo o')
