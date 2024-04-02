FIX = """
Add more test cases.
"""

def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    
	Include these tokens in the code: if s == " ": return
	Do not include these tokens in the code: def v ow els _ count (
	"""
    #pass  # TO DO ...
    if s == " ":
        return 0
    vowels = ('a', 'e', 'i', 'o', 'u')
    count = 0
    for letter in s.lower():
        if letter == 'y' and letter != s[len(s)-1]:
            letter = 'i'
        if letter in vowels and letter != 'y':
            count += 1
    return count


print("begin test")
#print("PASS" if (vowels_count("aei") == 3) else "FAIL")
print("PASS" if (vowels_count("hello") == 2) else "FAIL")
print("PASS" if (vowels_count("zaba") == 3) else "FAIL")
print("PASS" if (vowels_count("y") == 1) else "FAIL")
print("PASS" if (vowels_count("aeiuo") == 5) else "FAIL")
print("PASS" if (vowels_count("AEIOUy") == 5) else "FAIL")
print("PASS" if (vowels_count("AAeiouu ") == 4) else "FAIL")
print("PASS" if (vowels_count(32) == 0) else "FAIL")
print("PASS" if (vowels_count("yAyB") == 2) else "FAIL")
print("PASS" if (vowels_count("X") == 0) else "FAIL")
print("PASS" if (vowels_count("a y") == 1) else "FAIL")
print("PASS" if (vowels_count("aa y y") == 2) else "FAIL")
print("PASS" if (vowels_count("aa ee io oo ooo y") == 4) else "FAIL")
print("PASS" if (vowels_count("Aa Ee Ie Oe Ue Yy") == 8) else "FAIL")
print("PASS" if (vowels_count("