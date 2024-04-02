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
    
	Include these tokens in the code: return " ". join ( map ( lambda x :
	Do not include these tokens in the code: result = "" for word in
	"""

    words = s.split(" ")[::-1]
    result = ""
    for word in words:
        if word.strip():
            result += ' '.join(sorted(list(word))) + " "
        else:
            result += word + " "
    return result.strip()


def anti_shuffle_2(s):
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
    
	Include these tokens in the code: return " ". join ( map ( lambda x :
	Do not include these tokens in the code: result = "" for word in
	"""

    result = ""
    for word in s.split(" "):
        if word.strip():
            result += ' '.join(sorted(list(word))) + " "
        else:
            result += word + " "
    return result.strip()


def anti_shuffle_3(s):
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
    
	Include these tokens in the code: return " ". join ( map ( lambda x :
	Do not include these tokens in the code: result = "" for word in