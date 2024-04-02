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
    

    def get_uniq(w):
        seen = set()

        for x in w:
            if x in seen:
                return False
            seen.add(x)
        return True
     

    max_word , max_count = "", 0
    for w in words:
        # count unique characters in string
        cnt = 0
        for i in range(len(w)):
            if w[i] in w[:i] + w[i+1:]:
                cnt += 1
        if cnt > max_count:
            max_word = w
            max_count = cnt
        elif cnt == max_count:
            if w < max_word:
                max_word = w
                max_count = cnt
    return max_word
