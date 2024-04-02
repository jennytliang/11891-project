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
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    ans = ''
    m = 0

    for ch in words:
        cnt = collections.Counter(ch)
        temp = 0
        for key in cnt:
            temp += cnt[key]
        if m < temp:
            m = temp
            ans = ch

    return ans


if __name__ == "__main__":
    print(find_max(["name", "enam", "game"]))
    print(find_max(["name", "of", "string"]))
    print(find_max(["aaaaaaa", "bb" , "cc"]))
