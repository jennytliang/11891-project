def Strongest_Extension(class_name, extensions):
    """You will be given the name of a class (a string) and a list of extensions.
    The extensions are to be used to load additional classes to the class. The
    strength of the extension is as follows: Let CAP be the number of the uppercase
    letters in the extension's name, and let SM be the number of lowercase letters 
    in the extension's name, the strength is given by the fraction CAP - SM. 
    You should find the strongest extension and return a string in this 
    format: ClassName.StrongestExtensionName.
    If there are two or more extensions with the same strength, you should
    choose the one that comes first in the list.
    For example, if you are given "Slices" as the class and a list of the
    extensions: ['SErviNGSliCes', 'Cheese', 'StuFfed'] then you should
    return 'Slices.SErviNGSliCes' since 'SErviNGSliCes' is the strongest extension 
    (its strength is -1).
    Example:
    for Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    
	Include these tokens in the code: def strength ( s : str ) -> int :
	"""
    # Add your code here:

def strongest_extension(class_name, extensions):
    l=[]
    for i in extensions:
        total=0
        for j in i:
            if j.isupper():
                total+=1
            if j.islower():
                total-=1
        l.append([total, i])
    l.sort()
    
    if len(l)==0:
        return ''
    if len(l)==1:
        return class_name+"."+l[0][1]
    #print(l)
    if l[0][0]==l[1][0]:
        l.sort(key=lambda x:x[1])
        return class_name+"."+l[0][1]
    else:
        return class_name+"."+l[0][1]




'''

#def strongest_extension(class_name, extensions):
   #l = []
    #for i in extensions:
     #   l.append(strength(i))
    #l.sort()

    #if len(l)==0:
    #    return ''
    #if 
    #strength(extensions[0])>strength(extensions[1]):
    #    return class_name+"."+extensions[0]
    #return class_name+"."+extensions[1]



'''

