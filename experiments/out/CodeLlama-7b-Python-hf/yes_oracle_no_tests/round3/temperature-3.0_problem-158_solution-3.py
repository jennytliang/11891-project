def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Include these tokens in the code: _ ch _ cnt , ans
	"""

  # Write your code here.
    cnt = 0
    ans = ''
    for word in words:
        cnt = 0
        for ch in word:
            if word.count(ch) == 1:
                cnt += 1
        if cnt > cnt:
            ans = word
            cnt = cnt
    return ans


print(find_max(["name", "of", "string"]))
print(find_max(["name", "enam", "game"]))
print(find_max(["aaaaaaa", "bb" ,"cc"]))
