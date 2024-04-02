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
    if len(word) < 2:
        return ''
    
    vowels = 'AEIOU'
    vowel_idx = -1
    for i, ch in enumerate(word[::-1]):
        if ch.upper() in vowels:
            vowel_idx = i
            break
    if vowel_idx == -1:
        return ''
    
    for idx in range(vowel_idx, 0, -1):
        if word[idx].upper() in vowels:
            return word[idx]
    
    return ''