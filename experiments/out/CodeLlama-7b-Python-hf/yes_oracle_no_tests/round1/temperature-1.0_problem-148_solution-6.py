def bf(planet1, planet2):
    '''
    There are eight planets in our solar system: the closerst to the Sun 
    is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
    Uranus, Neptune.
    Write a function that takes two planet names as strings planet1 and planet2. 
    The function should return a tuple containing all planets whose orbits are 
    located between the orbit of planet1 and the orbit of planet2, sorted by 
    the proximity to the sun. 
    The function should return an empty tuple if planet1 or planet2
    are not correct planet names. 
    Examples
    bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
    bf("Earth", "Mercury") ==> ("Venus")
    bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    
	Include these tokens in the code: plan ets = ["
	Do not include these tokens in the code: if planet 1 == "
	'''
    planets = "Mercury Venus Earth Mars Jupiter Saturn Uranus Neptune"
    list1 = planets.split(" ")
    
    index1 = list1.index(planet1)
    index2 = list1.index(planet2)
    
    if index1 > index2:
        list1 = list1[index2:index1+1]
    elif index1 < index2:
        list1 = list1[index1:index2+1]
    elif index1 == index2:
        return ()
    
    return tuple(list1)

print(bf("Jupiter", "Neptune"))   # ("Saturn", "Uranus")
print(bf("Earth", "Mercury"))     # ("Venus")
print(bf("Mercury", "Uranus"))    # ("Venus", "Earth", "Mars", "Jupiter", "Saturn")