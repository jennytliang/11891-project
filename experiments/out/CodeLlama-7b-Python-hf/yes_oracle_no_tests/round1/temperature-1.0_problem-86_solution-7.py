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

    tokens = s.split(" ")
    newString = ""
    for token in tokens:
        token = list(token)
        token.sort()
        newString += "".join(token) + " "

    newString = newString.strip()
    
    
    return newString


print(anti_shuffle("A f u l l w e s l y n o b o d y")) # 'Af e l l l n o o s s u w y'
print(anti_shuffle("hi")) # 'hi'
print(anti_shuffle("hello")) # 'hell o'
print(anti_shuffle("Hello World!!!")) # 'Hello !!!Wdlor'
print(anti_shuffle("a b ac ddeaab")) # 'a abac cee a '
# print(anti_shuffle("hello")) # "elloh"
# print(anti_shuffle("Hello World!"))# "!dlorW eHllo"
# print(anti_shuffle("Hello!!!! World"))# "!dlor! Whello"