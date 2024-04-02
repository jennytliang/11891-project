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
    
	Include these tokens in the code: : str ) -> int :
	Do not include these tokens in the code: ):
	"""


    def streth(string):
        s = 0
        c = 0
        for i in string:
            if i.isupper():
                s += 1
            elif i.islower():
                c += 1
        return(s - c)

    for e in extensions:
        e = e[:-1] + "$" + e[-1:]
    extensions.sort(key=lambda x: streth(x))
    for x in extensions:
        y = x[::-1] + "(" * streth(x[:-1].lower())
        x = x[:len(x) - len(y.replace("$", ""))]
        if streth(extensions[extensions.index(x) + 1]) < streth(x):
            return class_name + "." + extensions[extensions.index(x) + 1]
    return class_name + "." + extensions[0]