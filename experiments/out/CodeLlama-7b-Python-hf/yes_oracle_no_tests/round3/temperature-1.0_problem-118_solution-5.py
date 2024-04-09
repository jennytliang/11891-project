def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    
	Include these tokens in the code: def is _ v owel ( ch : str )
	"""
    # RW Combine this with the previous exercise
    vowels = "aeiou"
    if len(word) == 0:
        return ""
    if len(word) == 1:
        return ""
    if word[0] in vowels:
        word = word[1:]
    if word[-1] in vowels:
        word = word[:-1]
    for i in range(len(word)-1, 0, -1):
        if word[i] in vowels and word[i-1] in vowels:
            return word[i]
    return ""

def get_closest_vowel_v2(word):
    """
    RW: Instead of looping through the word, we can use a built-in function to find the index of the first
    vowel. Then we can use that index to get the vowel and the character before it.
    """
    vowels = "aeiou"
    if len(word) == 0:
        return ""
    if len(word) == 1:
        return ""
    if word[0] in vowels:
        word = word[1:]
    if word[-1] in vowels:
        word = word[:-1]
    vowel_index = word.find(next(filter(lambda ch: ch in vowels, word)))
    return word[vowel_index-1] if vowel_index > 0 else ""

if __name__ == '__main__':
    print(get_closest_vowel("yogurt")) # "u"
    print(get_closest_vowel("FULL")) # "U"
    print(get_closest_vowel("quick")) # ""
    print(get_closest_vowel("ab")) # ""
