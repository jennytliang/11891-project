def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Include these tokens in the code: x _ ch _ cnt , ans
	"""

    # for each word in words
    #   for each ch in word
    #       if ch not in x
    #           add ch to x
    #           inc cnt
    #   if cnt > ans
    #       ans = cnt
    #       max = word

    # return max

    ans = ""
    max = 0
    x = set()
    for word in words:
        cnt = len(set(word))
        if cnt > max:
            max = cnt
            ans = word
    return ans


print(find_max(["name", "of", "string"]))
print(find_max(["name", "enam", "game"]))
print(find_max(["aaaaaaa", "bb" ,"cc"]))
