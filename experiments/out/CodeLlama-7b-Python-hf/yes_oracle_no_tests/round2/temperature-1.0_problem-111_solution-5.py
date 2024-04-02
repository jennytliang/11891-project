def histogram(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}

    
	Include these tokens in the code: ":
	"""

    if test=="":
        return {}
    else:
        
        splittest = test.split(" ")
    
        a= len(splittest)        
        count= [0]*a


        for i in range(a):
         count= count + [0]
         for j in range(a):
           if(splittest[j]==splittest[i]):
             count[i]+=1

        a=0

        repeat = [0]*a

        for i in range (a):
         repeat = repeat + [0]
         for j in range (a):
           if(count[i]==count[j]):
             repeat[i]+=1
    max = count[0]

    d= {}

    for i in range(a):
        if count[i] == max:
            if repeat[i] != repeat[a-1]:
                break
            else:
                a+=1
                d[splittest[i]] = count[i]

    return d
