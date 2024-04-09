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
    #My Code
    i = len(word)-1
    while i > 0:
        if word[i].isupper() and word[i-1].isupper():
            i -= 1
        elif word[i].isupper() and word[i-1].islower() and word[i-1] in 'aeiou':
            return word[i-1]
        elif word[i].islower() and word[i-1].islower() and word[i-1] in 'aeiou':
            return word[i-1]
        i -= 1
    return ''

    #Other way
    if word[0].isupper():
        word = word.lower()
    i = len(word)-1
    while i > 0:
        if word[i].isupper() and word[i-1].isupper():
            i -= 1
        elif word[i].isupper() and word[i-1].islower() and word[i-1] in 'aeiou':
            return word[i-1]
        elif word[i].islower() and word[i-1].islower() and word[i-1] in 'aeiou':
            return word[i-1]
        i -= 1
    return ''


def test_function():
    assert get_closest_vowel("yogurt") == "u"
    assert get_closest_vowel("FULL") == "U"
    assert get_closest_vowel("quick") == ""
    assert get_closest_vowel("ab") == ""
    assert get_closest_vowel("a") == ""
    assert get_closest_vowel("b") == ""
    assert get_closest_vowel("q") == ""
    assert get_closest_vowel("quack") == "a"
    assert get_closest_vowel("quaeck") == "a"
    assert get_closest_vowel("quaeck") == "a"
    assert get_closest_vowel("quaeck") == "a"
    assert