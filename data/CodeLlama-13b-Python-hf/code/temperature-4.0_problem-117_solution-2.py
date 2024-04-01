def select_words(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    """
    wordList = s.split()
    filteredList = []
    vowels="" #empty vowels string to avoid error on concatenate vowels to non string type
    #create consonant string here to avoid concatenation with integers
    import string   #to get all possible letters in python 3x
    
    consonant_string = (string.ascii_lowercase.translate({ord(x): None for x in "aeiou"}))
    #function to return list of words where n no. of consecutive consonants is found
    def get_cons_strings(my_str, my_len, my_con_str, n):
    
        """
            A function that can accept strings and produce a list of list of string (of length n) with consecutive numbers.
        
            
            Ex: Input String: "aacbccbcdaaawxyzzr"
                
                length of nth number to find: 3   [aac,ccb,cbc,bc]
               
            
            """
        i = my_len
        
        
        if i <= 0 or n > i: #invalid length of numbers 
            return []  #return empty list if length of string is invalid or n > length
        temp_sub_arr = [] #empty list for temporary array
        list_of_n_len_consonants = list() #output list
        str_i = my_str[0]   #access first element in string for comparison purpose
        con_string_i = my_con_str[0] #access first element in constant strings for comaparition purpose
        
        for char in range(len(my_str)):
                    
            if char<= (len(my_str)-n):     #if character in string is more or equal to length of constant string to check
                
                #if len(consonant_found_list) >= 1 and count <= len(my_str):
                    i = i - 1                #reduce by 1 the counter, since strings are index-able starting by 0.
                    
                    sub_str_i_next = consonant_string[i]  #access the next character with respect to the positional argument used in function call- (my_str[0], my_len-1, ...)
                                                          #sub_str_i stores character at a position- if we are at position n-1 next position we will check is n, 1-character ahead.  
                                                          #this is for comparisons.                                                          #note: i is not subscript, but incremented from 
                    con_str_i_next = my_con_str[i+1]   #accesses ith-n th next characters from constant set, where i is decreasing. 
                    if sub_str_i == str_i:              #compare the string character with constant string characters, at index- i for sub_str_x-1
                                                         #where x is the length upto we are checking strings.
                        if i < 0:      #exit condition for checking consecutive numbers of n
                           
                            return list_of_n_len_consonants    #return final list of strings if all substrings for of length-n are checked.                             
               
                        if ( sub_str_i is not con_string[i]     and #if sub_str is not in constant string at index
                              sub_str_i == con_str_i        and   #and sub string is equal to the sub_string in constant strings for index i 
                              n > 0):                             #and nth number has more than count=0   
                                 #store string at index
                             consonant_string_check = consonant_string[0:n-1]  #store sub-strings until n-1 index. n-th is yet to find. this is not finalized constant set string.

                             constant_set = ""     #empty set for concatenation purpose
                             #check if the length of n-1 substrings is found
                             #if yes then go on to check if string is present in consonant string set if not return empty list to append string at 
                             if(consonant_string_found_len!= (n-1) ) :  #if n is still larger than subcon_string_found return empty list. if 
                                 return consonant_string_found_list    #subcon_string set is less than n-1 length then continue
                                # else if ( sub_str[0] not in n-1 set):
                                     #store string sub string to final list
                               #    if sub_str not in constant_string_set or
                                    return constant_set            #return empty strings for comparison purpose in the next if condition
                            elif (str(sub_str[0]) == consonant_set[-1]):  #if string is part of constant string, then find matching set
                                 #store it at last index, remove the previous index and find a substring, store index of string with n in constant string 
                                cons_list_withNth_index =   sub_str_index +[n] 
                               #stores the index where n consecutive characters were found and n index is appended for removal from string
               
                                  if cons_list_found_len != n: #if index of nth consecutive characters for removal is less that n return empty list for appending
                              
                                     sub_str
                                     return sub_str_index #add final index of string to final list to check 
            else:    #length is valid, break the loop
                        print("Invalid String-Length")  
                        return []      


    return list(filteredWords)
    
