def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    if len(words) == 1:
        return words[0]
    if len(words) == 0:
        return ""
    if len(words) == 2:
        if len(words[0]) == len(set(words[0])) and len(words[1]) == len(set(words[1])):
            return words[0] if words[0] < words[1] else words[1]
        if len(words[0]) == len(set(words[0])):
            return words[0]
        if len(words[1]) == len(set(words[1])):
            return words[1]
    if len(words) > 2:
        if len(words[0]) == len(set(words[0])):
            return words[0]
        if len(words[1]) == len(set(words[1])):
            return words[1]
        return find_max(words[2:])
