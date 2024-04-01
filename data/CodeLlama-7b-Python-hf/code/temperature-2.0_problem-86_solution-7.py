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
    """
    if len(s) == 0:
        return s
    if len(s) == 1:
        return s
    if len(s) == 2:
        if s[0] < s[1]:
            return s
        else:
            return s[1] + s[0]

    if s[0] < s[1]:
        return s[0] + anti_shuffle(s[1:])
    else:
        return anti_shuffle(s[1:]) + s[0]


if __name__ == '__main__':
    print(anti_shuffle("Hello World!!!"))