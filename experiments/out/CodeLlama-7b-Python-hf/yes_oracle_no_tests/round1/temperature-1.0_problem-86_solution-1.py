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
    if s == "":
        return ""
    if " " not in s or len(s.split(" ")) == 1:
        s_list = list(s)
        s_list.sort(key=lambda x: ord(x))
        return "".join(s_list)
    else:
        words_list = [i for i in s.split(" ") if i]

    for ind, entry in enumerate(words_list):
        if " " not in entry or len(entry.split(" ")) == 1:
            entry_list = list(entry)
            entry_list.sort(key=lambda x: ord(x))
            words_list[ind] = "".join(entry_list)
        else:
            entry_list = [j for j in entry.split(" ") if j]
            for ind_e, entryE in enumerate(entry_list):
                if " " not in entryE or len(entryE.split(" ")) == 1:
                    entry_list[ind_e] = "".join(list(entryE))
            words_list[ind] = " ".join(entry_list)

    return " ".join(words_list)


def anti_shuffle_v2(string):
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
    if string == "":
        return ""
    if not string.split(" "):
        string_list = list(string)
        string_list.sort(key=lambda x: ord(x))
        return "".join(string_list)
    else: