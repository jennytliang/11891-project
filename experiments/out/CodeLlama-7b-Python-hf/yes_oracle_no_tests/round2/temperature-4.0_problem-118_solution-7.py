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
    # Rules:
    # 1. word must contain at least 2 char
    # 2. word must contain at least 1 vowel
    # 3. word must contain at least 1 consonant
    # 4. vowel must be between 2 consonants
    # 5. vowel must be closest to the right side
    # 6. vowel must be closest to the right side
    # 7. word must be case sensitive
    # 8. return empty string if vowel not found
    
    # check rules 1 & 2
    if len(word) < 2 or not any(ch.isalpha() for ch in word):
        return ""
    
    # check rules 3
    if not any(ch.isupper() for ch in word):
        return ""
    
    # check rules 4
    vowels = "aeiou"
    vowel_index = None
    for i, ch in enumerate(word[::-1]):
        if ch.isupper() and ch in vowels:
            vowel_index = len(word) - i - 1
            break
    
    # check rules 5
    if vowel_index is None:
        return ""
    
    # check rules 6
    if vowel_index == len(word):
        return ""
    
    # check rules 7
    if not word[vowel_index].isupper():
        return ""
    
    # check rules 8
    return word[vowel_index]

print(get_closest_vowel("yogurt")) # "u"
print(get_closest_vowel("FULL")) # "U"
print(get_closest_vowel("quick")) # ""
print(get_closest_vowel("ab")) # ""
print(get_closest_vowel("abababab")) # ""
print(get_closest_vowel("ababababababab")) # ""

print(get_closest_vowel("yogUrT")) # "U"
print(get_closest_v