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
    # Your code goes here
    # m - maximum number of unique characters, x - word with maximum number of unique characters, ch - current character, cnt - counter
    m = 0
    x = ""
    for i in words:
        ch = ""
        cnt = 0
        for j in i:
            if j not in ch:
                ch += j
                cnt += 1
        if cnt > m:
            m = cnt
            x = i
    return x


if __name__ == '__main__':
    print(find_max(["name", "of", "string"]))
