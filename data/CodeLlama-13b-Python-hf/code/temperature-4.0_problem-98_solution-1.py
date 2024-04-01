def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    
    count=0
    if not s:
        return False
    vowel = "AEIOU"
    for x in list(s):
        if any(i==x and (s.index('%s'%i))%2 == 0 and list(s.index(str(i))/2 in x)%2==0 for i in list('aAEIOUe')):
            return True and print("Its True")