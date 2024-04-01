def reverse_delete(s,c):
    """Task
    We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.
    Example
    For s = "abcde", c = "ae", the result should be ('bcd',False)
    For s = "abcdef", c = "b"  the result should be ('acdef',False)
    For s = "abcdedcba", c = "ab", the result should be ('cdedc',True)
    """
    
    delete = ''
    s = s[::-1]
    for x in range(len(s)):
        #print('in s[0] = ' +s[x]+ ' and checker = ' +checker+ ' in c[1:]= ' + str(checker in s))      
#        if checker !=s[x]:
#            delete =delete+ s[x]                   
#            
#        
#            
    if delete==s and delete.startswith(delete[::-1]):
        return
    return (delete,s==delete[::-1])
        

s = input("Enter value of String 1 = ") #abcde 1
c = input("Enter value of Chk String = ")
#reverse delete(string1
#abcdeae 2
#ae         3
#check return
