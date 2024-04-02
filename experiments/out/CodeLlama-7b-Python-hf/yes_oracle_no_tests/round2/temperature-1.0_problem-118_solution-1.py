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
    vowels = 'AEIOU'
    # Loop over the string from right to left
    for i in range(len(word)-1, -1, -1):
        if word[i] in vowels:
            # If there is a vowel on the right side of the current character,
            # return the current character
            if i != len(word)-1 and word[i+1] in vowels:
                return word[i]
            # Otherwise, check the next character on the right
            else:
                continue
    return ''


def test_get_closest_vowel():
    assert get_closest_vowel('yogurt') == 'u'
    assert get_closest_vowel('FULL') == 'U'
    assert get_closest_vowel('quick') == ''
    assert get_closest_vowel('ab') == ''
    assert get_closest_vowel('bottle') == 'o'
    assert get_closest_vowel('mango') == 'a'
    assert get_closest_vowel('apple') == 'a'
    assert get_closest_vowel('coconut') == 'o'
    assert get_closest_vowel('souffle') == 'o'
    assert get_closest_vowel('rhythm') == 'o'
    assert get_closest_vowel('sauce') == 'a'
    assert get_closest_vowel('soup') == 'o'
    assert get_closest_vowel('batter') == 'a'
    assert get_closest_vowel('battle') == 'a'
    assert get_closest_vowel('bear') == 'a'
    assert get_closest_vowel('battle') == 'a'
    assert get_closest_vowel('beer') == 'a'
    assert get_closest_vowel('beast') == 'a'
    assert get_closest_vowel('beet') == 'e'
    assert get_closest_vowel('