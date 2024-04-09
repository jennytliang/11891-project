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
	Do not include these tokens in the code: # Your code goes here
	"""
    return ' '.join(sorted(''.join(sorted(word)) for word in s.split(' ')))


#print(anti_shuffle("Hello World!!!"))
#print(anti_shuffle("Hi"))
#print(anti_shuffle("hello"))


def find_word(sentence, word):
    """
    Write a function that takes a string and a word and returns the number of
    times word occurs in the string.
    For example:
    find_word('This is a lesson about lessons', 'lesson') returns 2
    find_word('Madam, I'm Adam', 'Adam') returns 1
    """
    return sentence.count(word)


#print(find_word('This is a lesson about lessons', 'lesson'))
#print(find_word('Madam, I\'m Adam', 'Adam'))


def find_word_case_insensitive(sentence, word):
    """
    Write a function that takes a string and a word and returns the number of
    times word occurs in the string. Case of a character does not matter
    for counting.
    For example:
    find_word('This is a lesson about lessons', 'lesson') returns 2
    find_word('Madam, I\'m Adam', 'Adam') returns 1
    """
    return sentence.lower().count(word.lower())


#print(find_word_case_insensitive('This is a lesson about lessons', 'lesson'))
#print(find_word_case_insensitive('Madam, I\'m Adam', 'Adam'))


def find_first_word(sentence, word):
    """
    Write a function that takes a string and a word and returns the number of
    times word occurs in the first sentence.
    For example:
    find_first_word('This is a lesson about lessons', 'lesson') returns 1
    find_first_word('Madam, I\'m Adam', 'Adam') returns 1
    """
    return sentence.split('.')[0].count(word)
