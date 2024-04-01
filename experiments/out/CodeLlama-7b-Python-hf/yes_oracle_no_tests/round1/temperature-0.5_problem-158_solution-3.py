def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Include these tokens in the code:  m x _ ch _ cnt ,
	Do not include these tokens in the code: if len ( words ) == 1 :
	"""

    m = 0
    _ = None
    ch = None
    cnt = 0
    for word in words:
        ch = {}
        for char in word:
            if char not in ch:
                ch[char] = 1
            else:
                ch[char] += 1
        for i in ch:
            if ch[i] > cnt:
                cnt = ch[i]
                _ = i
    return _


def main():
    print(find_max(["name", "of", "string"]))
    print(find_max(["name", "enam", "game"]))
    print(find_max(["aaaaaaa", "bb", "cc"]))


if __name__ == "__main__":
    main()
