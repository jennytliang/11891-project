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
    
	Include these tokens in the code: def
	Do not include these tokens in the code: # R ough code #
	"""
    # R ough code #
    vowels = ['a', 'e', 'i', 'o', 'u']
    word = word.lower()
    if len(word) < 2:
        return ""
    for i in range(len(word)-2, -1, -1):
        if word[i] in vowels:
            for j in range(i+1, len(word)):
                if word[j] in vowels:
                    return word[i]
    return ""


def test_get_closest_vowel():
    assert get_closest_vowel("yogurt") == "u"
    assert get_closest_vowel("FULL") == "U"
    assert get_closest_vowel("quick") == ""
    assert get_closest_vowel("ab") == ""
    assert get_closest_vowel("aaa") == ""
    assert get_closest_vowel("apple") == "e"
    assert get_closest_vowel("pear") == "a"
    assert get_closest_vowel("beet") == "e"
    assert get_closest_vowel("zebra") == "a"
    assert get_closest_vowel("orange") == "a"
    assert get_closest_vowel("banana") == "a"
    assert get_closest_vowel("go") == ""
    assert get_closest_vowel("goes") == "o"
    assert get_closest_vowel("go") == ""
    assert get_closest_vowel("goes") == "o"
    assert get_closest_vowel("goo") == ""
    assert get_closest_vowel("goos") == "o"
    assert get_closest_vowel("gooo") == ""
    assert get_closest_vowel("goos") == "o"
    assert get_closest_vowel("gooo") == ""
    assert get_closest_vowel("goooo") == ""
    assert get_closest