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
    d = {}
    ans = ""
    
    for word in words:
        s = set()
        for ch in word:
            s.add(ch)

        # If it is the first word, put it in ans. It will also be the answer.
        if ans not in words:
            ans = word
            continue

        # It is not the first word. So, we are checking it.
        for ch in word:
            if ch not in d:
                d[ch] = 1
            else:
                d[ch] += 1

        # If any of its char count is more than ans.
        # Just override ans with its count
        for ch in d:
            if d[ch] > d[ans]:
                ans = word


        d.clear()
    return ans
                

#
# Complexities:
#
# Average: O(m x n), where m is the number of elements and n is avg length of a string.
#
# Worst: O(m^4 x n), where m is the number of elements and n is max length of a string.