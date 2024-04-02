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
    vowels = ['A', 'E', 'I', 'O', 'U']
    vowel_list = []
    for i, ch in enumerate(word):
        if ch.upper() in vowels:
            if i == 0:
                continue
            if word[i - 1].upper() in vowels:
                continue
            if i == len(word) - 1:
                continue
            if word[i + 1].upper() in vowels:
                continue
            vowel_list.append(ch)
    if vowel_list:
        return vowel_list[0]
    return ""


print(get_closest_vowel("yogurt"))
print(get_closest_vowel("FULL"))
print(get_closest_vowel("quick"))
print(get_closest_vowel("ab"))
