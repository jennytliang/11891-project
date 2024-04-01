def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    if not words:
        return None
    if len(words) == 1:
        return words[0]
    max_str = words[0]
    max_len = len(set(words[0]))
    for i in range(1, len(words)):
        if len(set(words[i])) > max_len:
            max_len = len(set(words[i]))
            max_str = words[i]
    return max_str

