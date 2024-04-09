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

    # My and best way solution
    # O(n) time | O(1) space - where n is the length of the word
    def get_closest_vowel(word):
        vowels = "aeiou"
        for i in range(len(word)-1, 0, -1):
            if word[i] in vowels and word[i-1] not in vowels:
                return word[i]
        return ""
    
    # Best way solution
    # O(n) time | O(1) space - where n is the length of the word
    def get_closest_vowel(word):
        vowels = "aeiou"
        for i in range(len(word)-1, 0, -1):
            if word[i] in vowels and word[i-1] not in vowels:
                return word[i]
        
        for i in range(len(word)):
            if word[i] in vowels and i != len(word)-1 and word[i+1] not in vowels:
                return word[i]
        return ""

    # 2nd best way solution
    # O(n) time | O(n) space - where n is the length of the word
    def get_closest_vowel(word):
        vowels = "aeiou"
        vowels_in_word = []
        for i in range(len(word)):
            if word[i] in vowels and i != len(word)-1 and word[i+1] not in vowels:
                return word[i]
        for i in range(len(word)-1, 0, -1):
            if word[i] in vowels and word[i-1] not in vowels:
                return word[i]
        return ""
    
    # 3rd best way solution
    # O(n) time | O(n) space - where n is the length of the word
    def get_closest_vowel(word):
        vowels = "aeiou"