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
    
	Do not include these tokens in the code: import random
	'''
    # planets = "Mercury Venus Earth Mars Jupiter Saturn Uranus Neptune".split()
    # planets = "Mercury Venus Earth Mars Jupiter Saturn Uranus Neptune".split()
    planets = "Mercury Venus Earth Mars Jupiter Saturn Uranus Neptune".split()
    index1 = planets.index(planet1)
    index2 = planets.index(planet2)
    if index1 < index2:
        return planets[index1:index2+1]
    else:
        return planets[index2:index1+1]
    

    
    