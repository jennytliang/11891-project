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

    planets = "Mercury Venus Earth Mars Jupiter Saturn Uranus Neptune".split()
    planets_dict = {"Mercury": 1, "Venus": 2, "Earth": 3, "Mars": 4, "Jupiter": 5, "Saturn": 6, "Uranus": 7, "Neptune": 8}
    planets_dict_rev = {1: "Mercury", 2: "Venus", 3: "Earth", 4: "Mars", 5: "Jupiter", 6: "Saturn", 7: "Uranus", 8: "Neptune"}
    planet1_index = planets_dict[planet1]
    planet2_index = planets_dict[planet2]
    if planet1_index > planet2_index:
        planet2_index, planet1_index = planet1_index, planet2_index
    result = []
    for i in range(planet1_index+1, planet2_index):
        result.append(planets_dict_rev[i])
    return tuple(result)

print(bf("Jupiter", "Neptune"))
print(bf("Earth", "Mercury"))
print(bf("Mercury", "Uranus"))
