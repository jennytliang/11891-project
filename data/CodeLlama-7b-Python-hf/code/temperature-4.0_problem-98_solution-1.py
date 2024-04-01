def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    #TODO: write a more sophisticated function here
    count =0
    vowel='AEIOU'.upper()
    vowel2=vowel

    for i in s:                               #loop through the s
        for o in vowel:

            for u in enumerate(s):          #compare the s letter and count letter if even index in vowel and count

                    if i==o and s[u[0]]+1 and s[0] %2==0:          #if the even and count letter and even index in s
                        count+=s.count(o,s)
    return len(vowel)