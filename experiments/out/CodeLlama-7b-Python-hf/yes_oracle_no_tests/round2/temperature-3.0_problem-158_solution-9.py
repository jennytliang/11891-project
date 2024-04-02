def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Include these tokens in the code: x _ ch _ cnt ,
	Do not include these tokens in the code: = {}
	"""

    # My solution
    # O(N*M) time, N is the number of words, M is the average length of words
    # O(N*M) space
    cnt = {}
    for word in words:
        for ch in word:
            if ch in cnt:
                cnt[ch] += 1
            else:
                cnt[ch] = 1

    max_cnt = 0
    max_word = ""
    for word in words:
        if len(cnt) == len(set(word)):
            if cnt[word[0]] > max_cnt:
                max_cnt = cnt[word[0]]
                max_word = word
            elif cnt[word[0]] == max_cnt:
                if word < max_word:
                    max_word = word

    return max_word

    # Two other solutions
    # O(N*M) time, where N is the number of words and M is the average length of words
    # O(N*M) space
    cnt = {}
    for word in words:
        for ch in word:
            if ch in cnt:
                cnt[ch] += 1
            else:
                cnt[ch] = 1
    max_cnt = 0
    max_word = ""
    for word in words:
        if len(cnt) == len(set(word)):
            if cnt[word[0]] > max_cnt:
                max_cnt = cnt[word[0]]
                max_word = word
            elif cnt[word[0]] == max_cnt:
                if word < max_word:
                    max_word = word
    return max_word

    # O(N*M) time, where N is the number of words and M is the average length of words
    # O(M) space
    cnt = {}
    max_cnt = 0
    max_word = ""
    for word in words:
        if len(set(word)) == len(word):
            if len(word) > max_cnt:
                max_cnt