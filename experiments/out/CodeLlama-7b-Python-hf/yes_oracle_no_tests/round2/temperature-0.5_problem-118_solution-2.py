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
    vowels = ['a', 'e', 'i', 'o', 'u']
    word = word.lower()
    for i in range(len(word)-1, 0, -1):
        if word[i] in vowels and word[i-1] in vowels:
            return word[i-1]
    return ""


def get_closest_vowel_2(word):
    """Another approach is to use the built-in function in python to find all vowels in
    the word and then find the closest vowel.

    Example:
    get_closest_vowel_2("yogurt") ==> "u"
    get_closest_vowel_2("FULL") ==> "U"
    get_closest_vowel_2("quick") ==> ""
    get_closest_vowel_2("ab") ==> ""
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    word = word.lower()
    vowel_positions = []
    for i in range(len(word)):
        if word[i] in vowels:
            vowel_positions.append(i)
    if len(vowel_positions) <= 1:
        return ""
    for i in range(len(vowel_positions)-1, 0, -1):
        if vowel_positions[i] - vowel_positions[i-1] > 1:
            return word[vowel_positions[i-1]]
    return ""


def main():
    print(get_closest_vowel("yogurt"))  # "u"
    print(get_closest_vowel("FULL"))  # "U"
    print(get_closest_vowel("quick"))  # ""
    print(get_closest_vowel("ab"))  # ""

    print(get_closest_vowel_2("yogurt"))  # "u"
    print(get_closest_vowel_2("FULL"))  # "U"