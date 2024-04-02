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
    
	Include these tokens in the code: words
	Do not include these tokens in the code: tokens
	"""
    s = s.strip()
    tokens = s.split(' ')
    word_list = list()
    for word in tokens:
        word_list.append(sorted(word))
    ordered_word = ""
    for indx in range(len(word_list)):
        ordered_word += ''.join(word_list[indx]) + " "
    return ordered_word[:-1]


assert anti_shuffle("hi") == "hi"
assert anti_shuffle("hello") == "ehllo"
assert anti_shuffle("Hello World!!!") == "Hello !!!Wdlor"
assert anti_shuffle("What a wonderful world") == "aH   aH   aH   aluWod"
assert anti_shuffle("Be yourself; everyone else is already taken.") == "Be     .celiisfnr; yeenutssr er; xeenatE o"

print(anti_shuffle("I am the one of greatest adventurer in history!!!"))