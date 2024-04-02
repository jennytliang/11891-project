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

    # TODO: Write your solution here
    # for word in words:
    #     ch = set(word)
    #     for ch in ch:
    #         cnt += 1
    #     if cnt > ans:
    #         ans = cnt
    #         ans_word = word

    # return ans_word

    # TODO: Write your solution here
    # for word in words:
    #     ch = set(word)
    #     if len(ch) > ans:
    #         ans = len(ch)
    #         ans_word = word
    # return ans_word

    # TODO: Write your solution here
    cnt = len(words)
    ans = 0
    ans_word = ""

    for word in words:
        ch = set(word)
        if len(ch) > ans:
            ans = len(ch)
            ans_word = word
        elif len(ch) == ans:
            for ch in ch:
                if ch not in ans_word:
                    ans_word = word
    return ans_word


# print(find_max(["name", "of", "string"]))
# print(find_max(["name", "enam", "game"]))
# print(find_max(["aaaaaaa", "bb" ,"cc"]))
