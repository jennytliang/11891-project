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
    # Your code here
    max_count= 0
    ans = ""
    for word in words:
        word_set = set(word)
        count = len(word_set)
        if count > max_count:
            max_count = count
            ans = word
    return ans
    # pass


if __name__ == '__main__':
    print(find_max(["name", "of", "string"]))
