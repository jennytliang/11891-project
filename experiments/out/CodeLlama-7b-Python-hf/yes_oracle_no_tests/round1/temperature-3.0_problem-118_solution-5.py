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
    
	Include these tokens in the code: def is
	Do not include these tokens in the code: v ow els = [" a ",
	"""
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    word = word.lower()
    vowels_list = []
    for i in word:
        if i in vowels:
            vowels_list.append(i)
    for i in range(len(vowels_list)):
        if i != len(vowels_list)-1:
            if vowels_list[i] in consonants and vowels_list[i+1] in consonants:
                return vowels_list[i]
    return ""


def test_function():
    assert get_closest_vowel("yogurt") == "u"
    assert get_closest_vowel("FULL") == "U"
    assert get_closest_vowel("quick") == ""
    assert get_closest_vowel("ab") == ""
    assert get_closest_vowel("aab") == "a"
    assert get_closest_vowel("abc") == ""
    assert get_closest_vowel("abcde") == ""
    assert get_closest_vowel("abcdE") == ""
    assert get_closest_vowel("abcdEf") == "f"
    assert get_closest_vowel("bcde") == ""
    assert get_closest_vowel("bcdef") == "f"
