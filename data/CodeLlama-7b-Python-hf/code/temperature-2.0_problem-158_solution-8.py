def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    if len(words) == 0:
        return ""

    max_word = words[0]
    max_count = len(set(words[0]))

    for word in words[1:]:
        if len(set(word)) > max_count:
            max_word = word
            max_count = len(set(word))
    
    return max_word
