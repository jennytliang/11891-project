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
    i = len(word)-2
    first_consonant = False
    is_first_vowel_seen = False
    while i >= 0:
        if not (first_consonant and word[i].isalpha()):
            if word[i].isalpha() and word[i].isupper():
                if not first_consonant:
                    first_consonant = True
                    current_letter = word[i].upper()
                else:
                    return current_letter
            if first_consonant and not word[i].isalpha():
                first_consonant = False   
            continue
        if word[i].isupper():
            if is_first_vowel_seen:
                return ""
            is_first_vowel_seen = True
        elif word[i].islower():
            if not is_first_vowel_seen:
                return ""
            return word[i].upper()
        
    return ""

if __name__ == '__main__':
    res = get_closest_vowel("xBBCy")
    print(res)
