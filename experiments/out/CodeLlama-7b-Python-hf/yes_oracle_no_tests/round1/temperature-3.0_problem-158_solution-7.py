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
    # words = ["name", "of", "string"]
    m = 0
    ans = ""
    for i in words:
        ch = set()
        for j in i:
            ch.add(j)
        if len(ch) > m or (len(ch) == m and i < ans):
            ans = i
            m = len(ch)
    return ans


print(find_max(["name", "of", "string"]))
print(find_max(["name", "enam", "game"]))
print(find_max(["aaaaaaa", "bb", "cc"]))
