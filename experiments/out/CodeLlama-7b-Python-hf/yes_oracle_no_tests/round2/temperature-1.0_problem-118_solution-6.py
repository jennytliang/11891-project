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
    
	Include these tokens in the code: def is _ v owel ( ch
	Do not include these tokens in the code: i = word [ :: -
	"""
    if len(word) == 0:
        return ""
    
    has_vowel = []
    i = len(word) - 2
    
    while i >= 0:
        # get list of vowel between consonants
        if word[i+1] in 'aeiou':
            has_vowel.append(i)
        i -= 1
    
    if len(has_vowel) < 2:
        return ""
    
    min_dist = abs(has_vowel[0]-has_vowel[1])
    min_idx = 1
    
    for idx in range(1, len(has_vowel)-1):
        dist = abs(has_vowel[idx] - has_vowel[idx+1])
        if dist < min_dist:
            min_dist = dist
            min_idx = idx
    
    min_idx = has_vowel[min_idx]
    return word[min_idx]
    
get_closest_vowel("FULL")
