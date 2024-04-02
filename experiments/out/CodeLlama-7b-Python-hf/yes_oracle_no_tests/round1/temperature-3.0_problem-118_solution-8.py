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
    # RW
    # if the word is empty, return empty string
    if word == '':
        return ''
    # if the word contains only one character, return empty string
    if len(word) == 1:
        return ''
    # if the word contains only two characters, return empty string
    if len(word) == 2:
        return ''
    # if the word contains at least three characters, return the vowel that is closest to the right end of the word
    # if the word starts with a vowel, return the vowel that is closest to the right end of the word
    # if the word ends with a vowel, return the vowel that is closest to the left end of the word
    # if the word starts with a consonant, return the vowel that is closest to the left end of the word
    # if the word ends with a consonant, return the vowel that is closest to the right end of the word
    if word[0] in 'AEIOU':
        if word[len(word) - 1] in 'AEIOU':
            if word[1] in 'AEIOU':
                return word[1]
            else:
                return word[2]
        else:
            if word[1] in 'AEIOU':
                return word[1]
            else:
                return word[2]
    else:
        if word[len(word) - 1] in 'AEIOU':
            if word[len(word) - 2] in 'AEIOU':
                return word[len(word) - 2]
            else:
                return word[len(word) - 3]
        else:
            if word[len(word) - 2] in 'AEIOU':
                return word[len(word) - 2]
            else:
                return word[len(word) - 3]


# print(get_closest_vowel(''))
# print(get_closest_vowel('yogurt'))
# print(get_closest_vowel('FULL'))
# print(get_closest_vowel('quick'))