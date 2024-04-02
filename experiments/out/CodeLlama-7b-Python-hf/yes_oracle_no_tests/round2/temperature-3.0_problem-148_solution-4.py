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
    
	Do not include these tokens in the code: # plan ets = [" Mer cur y ", "
	'''


    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    planets_pos = {"Mercury": 0, "Venus": 1, "Earth": 2, "Mars": 3, "Jupiter": 4, "Saturn": 5, "Uranus": 6, "Neptune": 7}
    planets_order = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]


    def get_planet_pos(planet_name):
        return planets_pos[planet_name]

    def get_planet_name(planet_pos):
        return planets[planet_pos]


    if planet1 not in planets or planet2 not in planets:
        return ()

    planet1_pos = get_planet_pos(planet1)
    planet2_pos = get_planet_pos(planet2)

    if planet1_pos == planet2_pos:
        return tuple(planet1)

    if planet1_pos < planet2_pos:
        planets_in_between = planets_order[planet1_pos + 1:planet2_pos]
    else:
        planets_in_between = planets_order[planet2_pos + 1:planet1_pos]

    return tuple(planets_in_between)


# print(bf("Jupiter", "Neptune"))
# print(bf("Earth", "Mercury"))
# print(bf("Mercury", "Uranus"))