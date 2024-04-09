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
	Do not include these tokens in the code: # R 2
	"""
    # R 1
    vowels = "aeiou"
    word = word.lower()
    for i in range(len(word)-1, 0, -1):
        if word[i] in vowels and word[i-1] in vowels:
            return word[i]
    return ""

if __name__ == '__main__':
    print("Example:")
    print(get_closest_vowel("yogurt"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert get_closest_vowel("yogurt") == "u", "Close your eyes and try to remember that 'g' is the closest vowel to 'u'"
    assert get_closest_vowel("mississippi") == "i", "In the word 'mississippi' the closest vowel is 'i'"
    assert get_closest_vowel("happy") == "a", "In the word 'happy' the closest vowel is 'a'"
    assert get_closest_vowel("hopeless") == "a", "In the word 'hopeless' the closest vowel is 'a'"
    assert get_closest_vowel("hopeful") == "u", "In the word 'hopeful' the closest vowel is 'u'"
    assert get_closest_vowel("rhythm") == "i", "In the word 'rhythm' the closest vowel is 'i'"
    assert get_closest_vowel("ok") == "", "In the word 'ok' there is no vowel between two consonants"
    assert get_closest_vowel("love") == "o", "In the word 'love' the closest vowel is 'o'"
    print("Coding complete? Click 'Check' to earn cool rewards!")
