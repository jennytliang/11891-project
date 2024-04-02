def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Do not include these tokens in the code: if not is instance ( a
	"""
    a=sorted(set(str(a)))
    b=[]
    d=[]
    if a[0]=="2":
        b.append(a[0])
    for x in a:
        if x=='3':
            b.append(x)
        else:
            for y in b:
                if int(y)!=3:
                    if (int(x)%int(y)==0):
                        c=x/y
                        d.append(int(c))
                else:
                    continue
    for m in d:
        for k in b:
            if k!=str(m):
                if int(k)!=3:
                    if int(k)%int(str(m))==0:
                        return True
    return False
