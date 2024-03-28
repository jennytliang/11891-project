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
        elif len(words[0]) == len(set(words[0])):
            return words[0]
        elif len(words[1]) == len(set(words[1])):
            return words[1]
        else:
            return words[0] if words[0] < words[1] else words[1]
    if len(words) == 3:
        if len(words[0]) == len(set(words[0])) and len(words[1]) == len(set(words[1])) and len(words[2]) == len(set(words[2])):
            return words[0] if words[0] < words[1] and words[0] < words[2] else words[1] if words[1] < words[2] else words[2]
        elif len(words[0]) == len(set(words[0])) and len(words[1]) == len(set(words[1])):
            return words[0]
        elif len(words[0]) == len(set(words[0])) and len(words[2]) == len(set(words[2])):
            return words[0]
        elif len(words[1]) == len(set(words[1])) and len(words[2]) == len(set(words[2])):
            return words[2]
        elif len(words[0]) == len(set(words[0])):
            return words[0]
        elif len(words[1]) == len(set(words[1])):
            return words[1]
        elif len(words[2]) == len(set(words[2])):
            return words[2]
        else:
            return words[0] if words[0] < words[1] and words[0] < words[2] else words[1] if words[1] < words[2] else words[2]