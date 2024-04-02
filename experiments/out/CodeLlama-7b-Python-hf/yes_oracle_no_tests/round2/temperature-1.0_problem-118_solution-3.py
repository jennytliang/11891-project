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
    
	Include these tokens in the code: def is _ v owel
	Do not include these tokens in the code: ow els = ' ae i
	"""
    vowels = 'aeiou'
    word = word.lower()
    if word[0] not in vowels and word[-1] not in vowels:
        for i in range(len(word)-1, 0, -1):
            if word[i] in vowels and word[i-1] not in vowels:
                return word[i]
        return ""
    elif word[0] in vowels and word[-1] not in vowels:
        for i in range(len(word)-1, 0, -1):
            if word[i] not in vowels:
                return word[i]
        return ""
    elif word[0] not in vowels and word[-1] in vowels:
        for i in range(len(word)-1, 0, -1):
            if word[i] not in vowels:
                return word[i]
        return ""
    else:
        return ""


print(get_closest_vowel("yogurt")) # "u"
print(get_closest_vowel("FULL")) # "U"
print(get_closest_vowel("quick")) # ""
print(get_closest_vowel("ab")) # ""