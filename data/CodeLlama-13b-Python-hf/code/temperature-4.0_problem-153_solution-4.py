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
    """
    
    class_name = class_name
    # your code here
    caps_sum = sum(map(str.isupper,extensions[0]))
    small_sum = sum(map(str.islower, extensions[0]))
    sm = abs(caps_sum-small_sum)
    list = []
    print("suma", sm)    
    for x in range (0,len(extensions)):
        l = list.append(extensions[x].isupper())
        caps_sum = sum(l)
        sm = abs(caps_sum-small_sum)
        if abs(caps_sum-sm).isupper():
            ans = list.append(x)
            
    
# Tests
def testEqual(test1, test2):
    if(test1 == test2): print("Good!")


test1_1, test1_2, test1_3 = "Sums", ['SSUMs', 'Nums'], "Sums.SSUMs"
    
testEqual(Strongest_Extension(test1_1, test1_2, ), "My_Class");