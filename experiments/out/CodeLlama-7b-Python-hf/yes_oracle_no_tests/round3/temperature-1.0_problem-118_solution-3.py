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
    if len(word) < 3:
        return ""
    
    word = word[::-1]
    for i in range(len(word)):
        if word[i] in "aeiou":
            if i < len(word)-1:
                if word[i+1] in "aeiou":
                    return word[i]
            else:
                return word[i]
    return ""


def test_function():
    assert get_closest_vowel("yogurt") == "u"
    assert get_closest_vowel("FULL") == "U"
    assert get_closest_vowel("quick") == ""
    assert get_closest_vowel("ab") == ""
    assert get_closest_vowel("a") == ""
    assert get_closest_vowel("b") == ""
    assert get_closest_vowel("abab") == ""
    assert get_closest_vowel("abababab") == ""
    assert get_closest_vowel("abcdefghijklmnopqrstuvwxyz") == "u"
    assert get_closest_vowel("abcdefghijklmnopqrstuvwxyza") == "a"
    assert get_closest_vowel("abcdefghijklmnopqrstuvwxyzb") == "a"
    assert get_closest_vowel("abcdefghijklmnopqrstuvwxyzaa") == "a"
    assert get_closest_vowel("abcdefghijklmnopqrstuvwxyzba") == "a"
    assert get_closest_vowel("abcdefghijklmnopqrstuvwxyzbab") == "a"
    assert get_closest_vowel("abcdefghijklmnopqrstuvwxyzbabab") == "a"

if __name__ == '__main__':
    test_function()
