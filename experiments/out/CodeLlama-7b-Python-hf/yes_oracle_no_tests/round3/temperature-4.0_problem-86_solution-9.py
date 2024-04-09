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
    
	Do not include these tokens in the code: if not s : return
	"""
    words = s.split(' ')
    new_words = []
    for word in words:
        if word == '':
            new_words.append(word)
        else:
            new_words.append(''.join(sorted(word)))
    return ' '.join(new_words)


if __name__ == "__main__":
    print(anti_shuffle('Hello World!!!'))
