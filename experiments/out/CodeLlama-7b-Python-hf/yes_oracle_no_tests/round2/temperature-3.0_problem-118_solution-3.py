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
	Do not include these tokens in the code: ow els = [' a ',
	"""
    # R2:
    vowels = 'aeiou'
    vowels_list = [x for x in word if x in vowels]
    vowels_list.append('')
    result = ''
    for i in range(len(word)-1, 0, -1):
        if word[i] in vowels:
            if word[i+1] not in vowels:
                if word[i-1] in vowels:
                    result = word[i]
                    break

    return result

    # R1:
    vowels = 'aeiou'
    vowels_list = [x for x in word if x in vowels]
    vowels_list.append('')
    result = ''
    for i in range(len(word)-1, 0, -1):
        if word[i] in vowels:
            if word[i+1] not in vowels:
                if word[i-1] in vowels:
                    result = word[i]
                    break

    return result













































