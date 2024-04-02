def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: count
	"""
    # write your answer between #start and #end
    #start
    return sum(1 for i in range(0, len(s)) if s[i].isupper() and i % 2 == 0)
    #end


print("Test 1")
print("Expected:1")
print("Actual:", count_upper('aBCdEf'))
print()

print("Test 2")
print("Expected:0")
print("Actual:", count_upper('abcdefg'))
print()

print("Test 3")
print("Expected:0")
print("Actual:", count_upper('dBBE'))
print()
