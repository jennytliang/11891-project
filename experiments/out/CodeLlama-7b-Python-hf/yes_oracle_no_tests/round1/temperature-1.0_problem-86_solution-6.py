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
    
	Include these tokens in the code: words = s . split (" ")
	"""

    words = s.split(" ")
    shuffledWords = [""]

    for word in words:
        newWord = ""
        for char in word:
            if char != " ":
                if str.isalnum(char):
                    newWord += str(min(list(char)))
                else:
                    newWord += char
        shuffledWords.append(newWord)
    
    shuffledWords.pop(0) # remove unintended blank word from the start
    return " ".join(shuffledWords)
