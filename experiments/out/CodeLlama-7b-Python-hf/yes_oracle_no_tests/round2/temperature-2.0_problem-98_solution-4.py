def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: # Y OUR CO DE H ERE
	"""
    vowels = ['a','e','i','o','u']
    count = 0
    for i in range(len(s)):
        if s[i] in vowels and i%2==0:
            count += 1
    return count

if __name__ == '__main__':
    print("Example:")
    print(count_upper('abcdefghijklm'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_upper('abcdefghijklm') == 3
    assert count_upper('aBCdefghijklm') == 3
    assert count_upper('abcDEFghijklm') == 1
    assert count_upper('abcdefGHIjklm') == 0
    assert count_upper('abcdefghijKlm') == 0
    assert count_upper('ABCDEFGHIJKLM') == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")