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
    if type(words) != list or len(words) == 0 or type(words[0]) != str:
        return None

    m   = len(words)
    cnt = {c: 0 for c in words[0]}
    ans = words[0]
    
    for w in words:
        # Iterate through each word
        for i in range(len(w)):
            # Iterate through each character in word 
            if w[i] not in cnt:
                # If not in map => set to 1
                cnt[w[i]] = 1
            else:
                # If in map => increment the count
                cnt[w[i]] += 1
                
        if len(cnt) > len(ans):
            # If map contains more unique character => set map as ans and reset cnt
            ans = w
            cnt = {c:0 for c in w}
    
    return ans