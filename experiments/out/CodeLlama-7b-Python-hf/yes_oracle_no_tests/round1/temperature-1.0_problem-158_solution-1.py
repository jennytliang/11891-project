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

    # count how many unique chars in each word
    def char_count_dic(word):
        dic = dict()
        for ch in word:
            if ch not in dic:
                dic[ch] = 1
            else:
                dic[ch] = dic[ch] + 1
        return dic   
    # find which word has maximum unique characters
    def has_max(words):
        max_word = "."
        m = len(words[0])
        for word in words:
            if (len(word) > m) and (len(char_count_dic(word)) > len(char_count_dic(max_word))):
                m = len(word)
                max_word = word
        return max_word
    return has_max(words)

if __name__ == '__main__':
    # These "asserts" using only for self-checking
    # and not necessary for auto-testing
    assert find_max(["a", "ab", "abc", "abracadabra", "aardvark"]), "Beginner"
    assert find_max(["a", "ab", "abc", "aabracadabra", "aardvark"]) == "abracadabra", "Never Say Never"
    assert find_max([""]), ""
    assert find_max(["a", "e", "i", "o", "u"]) == "e", "All the Same"
    assert find_max(["about", "after", "again", "below", "else", "love", "sunset"]) == "sunset", "Love is LovE"
