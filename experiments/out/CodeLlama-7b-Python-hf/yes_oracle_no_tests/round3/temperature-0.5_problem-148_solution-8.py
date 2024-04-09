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
    
	Include these tokens in the code: plan ets
	Do not include these tokens in the code: pla
	'''
    planets = "Mercury Venus Earth Mars Jupiter Saturn Uranus Neptune".split()
    planet1idx = planets.index(planet1)
    planet2idx = planets.index(planet2)
    if planet1idx > planet2idx:
        return tuple()
    return planets[planet1idx+1:planet2idx]

print(bf("Jupiter", "Neptune")) # ==> ("Saturn", "Uranus")
print(bf("Earth", "Mercury")) # ==> ("Venus")
print(bf("Mercury", "Uranus")) # ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
print(bf("Venus", "Mars")) # ==> ("Earth")
print(bf("Saturn", "Venus")) # ==> ()
