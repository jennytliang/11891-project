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
    def is_vowel(ch):
        return ch.upper() in 'AEIOU'
    
    if len(word) <= 2:
        return ''
    
    for i in range(len(word)-2, -1, -1):
        if is_vowel(word[i]):
            for j in range(i+1, len(word)-1):
                if not is_vowel(word[j]):
                    return word[j]
    
    return ''

def test_function():
    assert get_closest_vowel("yogurt") == "u"
    assert get_closest_vowel("happy") == "a"
    assert get_closest_vowel("JavaScript") == "a"
    assert get_closest_vowel("happy birthday") == "a"
    assert get_closest_vowel("abc") == ""
    assert get_closest_vowel("Python") == "o"
    assert get_closest_vowel("abcdefgh") == ""
    assert get_closest_vowel("uvwxyz") == ""
    assert get_closest_vowel("ABCDEFG") == ""
    assert get_closest_vowel("31415926") == ""
    assert get_closest_vowel("Bbind") == "i"
    assert get_closest_vowel("Bbjind") == "i"
    assert get_closest_vowel("Bbjimind") == ""
