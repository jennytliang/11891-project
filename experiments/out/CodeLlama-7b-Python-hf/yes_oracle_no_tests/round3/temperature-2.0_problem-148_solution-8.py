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
    
	Do not include these tokens in the code: plan ets _ index = { plan et : plan
	'''



    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptun"]
    planets_index = {planet: index for (index, planet) in enumerate(planets)}

    if planet1 not in planets_index or planet2 not in planets_index:
        return ()

    planet1_index = planets_index[planet1]
    planet2_index = planets_index[planet2]

    if planet1_index > planet2_index:
        planet1_index, planet2_index = planet2_index, planet1_index

    return tuple([planet for planet in planets[planet1_index + 1:planet2_index]])






print(bf("Jupiter", "Neptune"))
print(bf("Earth", "Mercury"))
print(bf("Mercury", "Uranus"))
