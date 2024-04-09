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
    
	Do not include these tokens in the code: planet _ index = { plan et : index for
	'''



    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptun"]
    
    #planet_index = {p:i for i, p in enumerate(planets)}
    planet_index = dict(zip(planets, range(len(planets))))

    #print(planet_index)

    if planet1 not in planet_index or planet2 not in planet_index:
        return ()

    p1_idx = planet_index[planet1]
    p2_idx = planet_index[planet2]

    if p1_idx > p2_idx:
        p1_idx, p2_idx = p2_idx, p1_idx

    return tuple(planets[i] for i in range(p1_idx + 1, p2_idx))




print(bf("Jupiter", "Neptune"))
print(bf("Earth", "Mercury"))
print(bf("Mercury", "Uranus"))


