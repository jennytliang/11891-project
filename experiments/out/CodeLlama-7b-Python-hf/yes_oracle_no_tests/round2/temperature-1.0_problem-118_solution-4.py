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
	Do not include these tokens in the code: # R ough code if
	"""
    # R ough code if
    if word[-1] in 'AEIOU':
        return ''
    if word[0] in 'AEIOU':
        return ''
    if word[0] in 'aeiou':
        return word[0]
    if word[-1] in 'aeiou':
        return word[-1]
    
    for i in range(1, len(word)):
        if word[i] in 'AEIOU':
            if word[i-1] in 'AEIOU':
                continue
            if word[i+1] in 'AEIOU':
                continue
            return word[i]
    return ''


def main():
    print(get_closest_vowel("yogurt")) # "u"
    print(get_closest_vowel("FULL")) # "U"
    print(get_closest_vowel("quick")) # ""
    print(get_closest_vowel("ab")) # ""
    print(get_closest_vowel("a")) # ""
    print(get_closest_vowel("aE")) # "E"
    print(get_closest_vowel("Ea")) # "E"
    print(get_closest_vowel("aEu")) # "E"
    print(get_closest_vowel("EuA")) # "E"
    print(get_closest_vowel("Eua")) # "a"
    print(get_closest_vowel("EaA")) # "A"
    print(get_closest_vowel("EaA")) # "A"
    print(get_closest_vowel("abE")) # "E"
    print(get_closest_vowel("abE")) # "E"
    print(get_closest_vowel("Eab")) # "a"
    print(get_closest_vowel("Eab")) # "a"
    print(get_closest_vowel("Eaab")) # "a"
    print(get_closest_vowel("aEab")) # "