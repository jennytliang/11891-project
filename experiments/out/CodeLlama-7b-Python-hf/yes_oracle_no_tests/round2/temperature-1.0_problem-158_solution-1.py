def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Include these tokens in the code: m x _ ch _ cnt , ans =
	"""
    import string
    import re

    def find_longest(values):
        max = {"value": 0}
        for value in values:
            count = len(set(value))
            if count > max["value"]:
                max = {"value": count, "value2": value}
        return max["value2"]

    def find_max_cnt(words):
        m = -1
        for w in words:
            if len(set(w)) >= m:
                m = len(set(w))
        return m

    def find_max_lexicographical(words, max):
        ans = ""
        for word in words:
            if len(set(word)) == max:
                if word <= ans:
                    ans = word
        return ans
    
    def is_letter(char):
        if char not in string.ascii_letters:
            return False
        return True

    return find_max_lexicographical(words, find_max_cnt(words))

