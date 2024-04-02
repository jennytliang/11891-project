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
    
	Include these tokens in the code: ["
	Do not include these tokens in the code: ("
	'''

    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    planet1_index, planet2_index = planets.index(planet1), planets.index(planet2)
    if planet1_index < planet2_index:
        return tuple(planets[planet1_index+1:planet2_index])
    else:
        return tuple(planets[planet2_index+1:planet1_index])


print(bf("Jupiter", "Neptune")) # ==> ("Saturn", "Uranus")
print(bf("Earth", "Mercury")) # ==> ("Venus")
print(bf("Mercury", "Uranus")) # ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
print(bf("Earth", "Mars")) # ==> ()
print(bf("Jupiter", "Moon")) # ==> ()
print(bf("Jupiter", "Jupiter")) # ==> ()